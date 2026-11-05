# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

## Declared stretch items

Before implementing the stretch work, I committed to all three items:

1. **A third signal:** lexical rhythm, implemented in
   `lexical_signal.py::lexical_signal`. The final score weights the model
   signal at 0.50, the style signal at 0.35, and lexical rhythm at 0.15.
   The model signal gets the most weight because it directly measures
   predictability; the two cheaper text-shape signals provide corroborating
   evidence without allowing either one to dominate.
2. **`GET /content/<id>`:** returns the current status and the stored decision
   for one content item.
3. **A verified-human path:** `POST /verify-human` is an extra confirmation
   step that issues a credential. A writer can include that credential when
   submitting work, and the credential is shown on the submission and in
   `GET /content/<id>`.

These are implemented below and the sample requests/responses account for
the new fields and routes.

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer sends JSON containing `text` and `creator_id` to `POST /submit`.
2. The route extracts the text and creates a unique `content_id` for the
   submission.
3. `detector.model_signal(text)` measures how predictable the text is to the
   local language model and returns `model_score`.
4. `stylometry.style_signal(text)` measures sentence-length variation,
   vocabulary repetition, and punctuation density and returns `style_score`.
5. `lexical_signal.lexical_signal(text)` measures variation in word lengths
   as a third, independent text-shape signal.
6. `scoring.combine_signals(model_score, style_score, lexical_score)` applies
   the configured 50/35/15 weighted average and produces `combined_score`.
7. `scoring.score_to_label(combined_score)` maps that score to `human`,
   `unsure`, or `ai`, along with a full sentence a reader can understand.
8. The route writes the decision and all three signal scores to
   `logs/audit.jsonl`, then returns the content ID, scores, guess, confidence,
   label, and verified-human credential state. If the writer appeals,
   `POST /appeal` appends an `under_review` event for the same content ID.
   `GET /content/<id>` reads those entries and reports the item's current
   status.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Language-model predictability (perplexity), converted to
a score from 0.0 to 1.0. Higher means the local model finds the writing easier
to predict and therefore more AI-like.

**Why that might differ between human and AI writing:** Generated writing
tends to choose probable next words and familiar sentence patterns, while
human writing can contain more surprising personal choices and abrupt turns.

**What it can't see:** Predictability is not authorship. Plain writing by a
real person, including writing by a second-language writer, can be highly
predictable; unusual or heavily edited AI text can be less predictable.

### Signal two — the style signal

**What it measures:** Sentence-length spread, type-token ratio (unique words
divided by total words), and varied punctuation density. These are normalized
and combined into a 0.0 to 1.0 score, where higher means more AI-like.

**Why that might differ between human and AI writing:** Generated prose often
has regular sentence lengths, repeated likely vocabulary, and restrained
punctuation. Human prose is often more uneven and idiosyncratic.

**What it can't see:** It cannot understand meaning or identify authorship.
Typos, sentence splitting, punctuation edits, or inserted quotations can
change the score without changing the substance.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the three
     signals disagree? -->

**The rule:** The final score is a weighted average of three scores. The
signals point in the same direction, so a higher result always means more
AI-like. Disagreement is retained as uncertainty in the middle rather than
allowing any one signal to override the others.

**The numbers:** `0.50 * model_score + 0.35 * style_score + 0.15 *
lexical_score`, rounded to four decimal places and clamped to the 0.0–1.0
range. The weights come from the three `WEIGHT_*_SIGNAL` settings in
`config.py`.

**Where it lives:** `scoring.py::combine_signals`

### Signal three — lexical rhythm

**What it measures:** The coefficient of variation in word lengths, converted
to an AI-likelihood score. A narrow mix of word lengths scores more AI-like;
more varied word lengths score more human-like.

**Why it might differ:** Generated prose often uses a consistent register and
word length, while an individual writer commonly mixes short connective words
with longer, specific terms.

**What it can't see:** It cannot understand meaning or authorship. Technical
writing, a second-language writer, or deliberate editing can produce either
word-length pattern.

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where two of my three signals split, and what my rule does with it:** The
clearly human sample in the calibration run produced a model score of `0.5844`
and a style score of `0.4831`. The model leaned AI-like while stylometry
leaned more human-like; the weighted average preserves that disagreement
instead of making either signal decisive on its own.

**Baseline calibration run (the original two-signal measurements are retained
for comparison; live submissions now add the lexical score shown in responses):**

| Input | Model score | Style score | Combined score |
|---|---:|---:|---:|
| Clearly AI | 0.6987 | 0.5574 | 0.6280 |
| Clearly human | 0.5844 | 0.4831 | 0.5337 |
| Formal human | 0.3785 | 0.6154 | 0.4970 |
| Lightly edited AI | 0.3486 | 0.4270 | 0.3878 |

The formal human sample is a useful disagreement case in the opposite
direction: its style score was higher than its model score. The lightly edited
AI sample also shows the blind spots of both signals, landing much closer to
the human side than its source category suggests.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 through 0.35, including both endpoints | We think this was probably written by a person. |
| unsure | above 0.35 and below 0.65 | We cannot confidently determine whether this was written by a person or generated by AI. |
| high-confidence AI | 0.65 through 1.00, including both endpoints | We think this was probably written by an AI system. |

**Why I worded the "unsure" one this way:**
It admits that the system cannot establish authorship from these signals
instead of turning uncertainty into an accusation. It also avoids technical
terms such as "threshold" and "confidence score."



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, both signal
     scores, and the combined score. Unit 8's tools read the two component
     scores directly, so leaving them out costs the later diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must support diverse inputs. Additionally, overall performance depends on multiple variables.", "creator_id": "calibration-ai"}'
```

```json
{"combined_score":0.6062,"confidence":0.2124,"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","credential_id":null,"guess":"unsure","label":"We cannot confidently determine whether this was written by a person or generated by AI.","lexical_score":0.412,"model_score":0.6987,"style_score":0.5574,"verified_human":false}
```

**The audit log**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{"count":2,"entries":[{"combined_score":0.628,"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","creator_id":"calibration-ai","guess":"unsure","label":"We cannot confidently determine whether this was written by a person or generated by AI.","model_score":0.6987,"status":"decided","style_score":0.5574,"timestamp":"2026-10-28T23:22:44+00:00"},{"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","creator_id":"calibration-ai","event":"appeal","reasoning":"I wrote this submission myself and request a human review.","status":"under_review","timestamp":"2026-10-28T23:22:44+00:00"}]}
```

**The appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "3de55966-615a-428c-b7f5-7bd8a963d749", "reasoning": "I wrote this submission myself and request a human review."}'
```

```json
{"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","message":"Your appeal has been recorded for review.","status":"under_review"}
```

### Current status lookup

After submission, the returned ID can be used to retrieve the current status:

```bash
$ curl "http://127.0.0.1:5000/content/3de55966-615a-428c-b7f5-7bd8a963d749"
```

```json
{"combined_score":0.6062,"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","creator_id":"calibration-ai","credential_id":null,"guess":"unsure","label":"We cannot confidently determine whether this was written by a person or generated by AI.","lexical_score":0.412,"model_score":0.6987,"status":"under_review","style_score":0.5574,"verified_human":false}
```

An unknown ID returns HTTP 404 with `{"error":"not_found",...}`.

### Verified-human path

The writer completes an extra confirmation step, which issues a credential:

```bash
$ curl -X POST http://127.0.0.1:5000/verify-human \
  -H "Content-Type: application/json" \
  -d '{"creator_id":"writer-7","confirmation":"I am a human writer"}'
```

```json
{"creator_id":"writer-7","credential_id":"vh-8f4d...","status":"verified"}
```

The writer includes that credential on the next submission:

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"creator_id":"writer-7","human_credential":"vh-8f4d...","text":"My submission text."}'
```

The response includes `"verified_human":true` and the same
`"credential_id":"vh-8f4d..."`; the credential is also stored in the audit
entry and returned by `GET /content/<id>`.

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{"count":2,"entries":[{"combined_score":0.628,"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","creator_id":"calibration-ai","guess":"unsure","label":"We cannot confidently determine whether this was written by a person or generated by AI.","model_score":0.6987,"status":"decided","style_score":0.5574,"timestamp":"2026-10-28T23:22:44+00:00"},{"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","creator_id":"calibration-ai","event":"appeal","reasoning":"I wrote this submission myself and request a human review.","status":"under_review","timestamp":"2026-10-28T23:22:44+00:00"}]}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked for help tracing the service from `POST /submit`
  through the detector, stylometry, scoring, label mapping, and audit log,
  including the blind spot of each signal and the false-positive appeal path.
- *What came back:* The response organized the pipeline into seven stages and
  identified that model predictability can accuse a plain human writer, while
  stylometry can be changed by sentence splitting, punctuation edits, or
  inserted quotations without changing meaning.
- *What I changed:* I used that trace to write the acceptance criteria in
  `criteria.md`, especially the false-positive limit, reachable-label check,
  appeal recording requirement, and explicit bad-input behavior. I kept the
  blind spots in the README rather than treating either signal as proof of
  authorship.

**Moment 2**

- *What I asked for:* I asked for a review of the three-signal implementation
  and for calibration of clearly AI, clearly human, formal human, and
  lightly edited AI samples, with both component scores shown.
- *What came back:* The calibration showed the formal-human sample splitting:
  the model score was `0.3785` while the style score was `0.6154`. It also
  showed that lightly edited AI text could land near the human side at
  `0.3486` model, `0.4270` style, and `0.3878` combined.
- *What I changed:* I used a 50/35/15 weighted average in
  `scoring.py::combine_signals` so disagreement remains visible as uncertainty
  instead of letting one imperfect signal override the other. I documented the
  numbers and the split case in the Signals and Scoring section, then added the
  three reader-facing labels and the appeal path.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

Ten submissions per minute leaves room for a writer to submit drafts and
revisions without waiting, while a burst of automated variations is stopped
quickly. The 200-per-day ceiling allows a busy writing day but limits a script
trying to map the thresholds over many hours.

**What a caller counts as:** `creator_id`. A script cannot evade the limit by
changing network addresses, while separate writers on one household network do
not share a bucket.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

The run produced 5 rate-limited requests out of 15 and wrote
`results/flood_2026-11-03_2112.md`. The 429 handler also wrote rejection entries
to the audit log. Three additional submissions and a missing-text request were
checked through `GET /log`; the three decisions had all nine required fields,
and the invalid request appeared as `missing_or_empty_text`.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The complete run contained 56 requests. I marked an attack **held** when the
service prevented the behavior named in `targets`, and **broke** when the
attack achieved that behavior. The result was **29 held and 27 broke**. The
27 broken cases were nine evasion attacks, two false positives, six malformed
inputs accepted as decisions, and ten flood submissions accepted before the
limiter rejected the final two.

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---:|---|---:|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.323 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.468 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.528 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.542 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.344 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.432 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.531 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.333 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.548 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.764 | **HELD** |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.556 | **HELD** |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.631 | **HELD** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.632 | **HELD** |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.647 | **HELD** |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.662 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.640 | **HELD** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.655 | **BROKE** |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.395 | **HELD** |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.395 | **HELD** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.260 | **HELD** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.491 | **HELD** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.443 | **HELD** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.397 | **HELD** |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.521 | **HELD** |
| MF01 | malformed | text is only whitespace | 400 | — | — | **HELD** |
| MF02 | malformed | text is a single character | 500 | — | — | **BROKE** |
| MF03 | malformed | text is control characters | 200 | human | 0.142 | **BROKE** |
| MF04 | malformed | text is only punctuation | 200 | human | 0.314 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.807 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.923 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.878 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | **HELD** |
| RQ01 | malformed | no text field at all | 400 | — | — | **HELD** |
| RQ02 | malformed | no creator_id | 400 | — | — | **HELD** |
| RQ03 | malformed | text is a number | 400 | — | — | **HELD** |
| RQ04 | malformed | text is a list | 400 | — | — | **HELD** |
| RQ05 | malformed | text is null | 400 | — | — | **HELD** |
| RQ06 | malformed | creator_id is an object | 400 | — | — | **HELD** |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | **HELD** |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | **HELD** |
| RQ09 | malformed | body is empty | 400 | — | — | **HELD** |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | **HELD** |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | **HELD** |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | **HELD** |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.263 | **BROKE** |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"combined_score":0.3232,"content_id":"848180af-a4c2-4525-aadb-834fd9435c4f","creator_id":"attacker_EV01","credential_id":null,"guess":"human","label":"We think this was probably written by a person.","lexical_score":0.1379,"model_score":0.1635,"status":"decided","style_score":0.6308,"timestamp":"2026-11-05T00:15:54+00:00","verified_human":false}
{"combined_score":0.3439,"content_id":"5d9e6154-83bd-4abc-928c-26f055164246","creator_id":"attacker_EV05","credential_id":null,"guess":"human","label":"We think this was probably written by a person.","lexical_score":0.1595,"model_score":0.3212,"status":"decided","style_score":0.4555,"timestamp":"2026-11-05T00:15:55+00:00","verified_human":false}
{"combined_score":0.7644,"content_id":"6fab9c11-8bc5-42e6-9645-93a4447c8f00","creator_id":"attacker_EV10","credential_id":null,"guess":"ai","label":"We think this was probably written by an AI system.","lexical_score":0.0544,"model_score":0.9792,"status":"decided","style_score":0.7619,"timestamp":"2026-11-05T00:15:57+00:00","verified_human":false}
{"combined_score":0.6622,"content_id":"131b23b9-c15d-4e6e-ad21-31d459347d14","creator_id":"attacker_FP05","credential_id":null,"guess":"ai","label":"We think this was probably written by an AI system.","lexical_score":0.1337,"model_score":0.8005,"status":"decided","style_score":0.6912,"timestamp":"2026-11-05T00:15:58+00:00","verified_human":false}
{"combined_score":0.6546,"content_id":"3243e031-fe96-459e-a74f-8bab882e9ce0","creator_id":"attacker_FP07","credential_id":null,"guess":"ai","label":"We think this was probably written by an AI system.","lexical_score":0.075,"model_score":0.8816,"status":"decided","style_score":0.5788,"timestamp":"2026-11-05T00:15:59+00:00","verified_human":false}
{"combined_score":0.1417,"content_id":"a6280831-7616-485c-bac3-edb464d5ec5d","creator_id":"attacker_MF03","credential_id":null,"guess":"human","label":"We think this was probably written by a person.","lexical_score":0.1667,"model_score":0.0,"status":"decided","style_score":0.3333,"timestamp":"2026-11-05T00:16:01+00:00","verified_human":false}
{"combined_score":0.9234,"content_id":"b19e43ea-69a0-4a95-b3e9-af92f299cd0e","creator_id":"attacker_MF06","credential_id":null,"guess":"ai","label":"We think this was probably written by an AI system.","lexical_score":0.5,"model_score":0.9969,"status":"decided","style_score":1.0,"timestamp":"2026-11-05T00:16:03+00:00","verified_human":false}
{"creator_id":"attacker_MF08","event":"rejected","limit":10000,"reason":"content_too_large","status":"rejected","timestamp":"2026-11-05T00:16:03+00:00"}
{"creator_id":"attacker_flood","event":"rejected","limit":"10 per 1 minute","reason":"rate_limited","status":"rejected","timestamp":"2026-11-05T00:16:05+00:00"}
{"creator_id":"attacker_RQ01","event":"rejected","reason":"missing_or_empty_text","status":"rejected","timestamp":"2026-11-05T00:16:03+00:00"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: **FP05**, the technical documentation written by
a person. It received `model_score=0.8005`, `style_score=0.6912`, and a
combined score of `0.6622`, just over the AI threshold, so the service told
that writer, “We think this was probably written by an AI system.” This is a
false accusation rather than an uncertainty result, and the log shows the
model and style signals agreeing even though the target says the author was
human.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | At most 1 of 10 | 0/10 | 0/10 | 0/10 | **MET** |
| 2. Score separation | AI mean at least 0.20 above human; 4/5 on each side of 0.50 | 4/5 AI above 0.50; human mean 0.427, AI mean 0.547 (gap 0.121) | 4/5; same scores | 4/5; same scores | **MISSED** |
| 3. All three labels reachable | 3 of 3 labels, with matching thresholds | 3/3 | 3/3 | 3/3 | **MET** |
| 4. Appeal changes status and records | 2/2 known appeals; 404 for unknown ID | 2/2; 404 | 2/2; 404 | 2/2; 404 | **MET** |
| 5. Bad input is rejected safely | 6 invalid requests return 400; oversized request returns 413 | 7/7 | 7/7 | 7/7 | **MET** |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

The following are the actual trial-1 JSON arrays from
`results/run_2026-11-04_1927_before.md`, produced by
`run_eval.py::main` (submissions go through `app.py::submit`; appeals use
`app.py::appeal`).

### Criterion 1 — my own writing

```json
[{"status":200,"guess":"unsure","confidence":0.0848,"model_score":0.4032,"style_score":0.6827,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I keep a short list of tasks beside my keyboard because the list helps"},{"status":200,"guess":"unsure","confidence":0.1718,"model_score":0.3523,"style_score":0.5881,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The bus was late again, so I walked the last six blocks with my coffee"},{"status":200,"guess":"unsure","confidence":0.2958,"model_score":0.3546,"style_score":0.4205,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I learned to repair small things from my grandfather. He never started"},{"status":200,"guess":"unsure","confidence":0.2352,"model_score":0.329,"style_score":0.5349,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"My first draft of the volunteer schedule was too tidy to use. People h"},{"status":200,"guess":"unsure","confidence":0.2604,"model_score":0.2897,"style_score":0.6427,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I prefer a notebook to a new productivity app for ideas that are not r"},{"status":200,"guess":"unsure","confidence":0.1122,"model_score":0.4006,"style_score":0.5619,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"At the farmers market I bought tomatoes because they smelled good, not"},{"status":200,"guess":"unsure","confidence":0.1932,"model_score":0.3821,"style_score":0.5048,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The room looked clean until I tried to find the charger. I emptied one"},{"status":200,"guess":"unsure","confidence":0.2706,"model_score":0.413,"style_score":0.4456,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I used to save every receipt in one envelope. It felt responsible, but"},{"status":200,"guess":"unsure","confidence":0.0944,"model_score":0.4037,"style_score":0.5825,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"When the rain started, our dog refused the usual route and pulled towa"},{"status":200,"guess":"unsure","confidence":0.0826,"model_score":0.4844,"style_score":0.7332,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I rewrote the note twice because the first version sounded certain and"}]
```

### Criterion 2 — score separation

```json
[{"status":200,"guess":"unsure","confidence":0.1718,"model_score":0.3523,"style_score":0.5881,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The bus was late again, so I walked the last six blocks with my coffee"},{"status":200,"guess":"unsure","confidence":0.2958,"model_score":0.3546,"style_score":0.4205,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I learned to repair small things from my grandfather. He never started"},{"status":200,"guess":"unsure","confidence":0.2352,"model_score":0.329,"style_score":0.5349,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"My first draft of the volunteer schedule was too tidy to use. People h"},{"status":200,"guess":"unsure","confidence":0.1122,"model_score":0.4006,"style_score":0.5619,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"At the farmers market I bought tomatoes because they smelled good, not"},{"status":200,"guess":"unsure","confidence":0.0826,"model_score":0.4844,"style_score":0.7332,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"I rewrote the note twice because the first version sounded certain and"},{"status":200,"guess":"unsure","confidence":0.1146,"model_score":0.6987,"style_score":0.5574,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The implementation of the proposed framework requires careful consider"},{"status":200,"guess":"unsure","confidence":0.005,"model_score":0.5847,"style_score":0.5121,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"A successful organization benefits from clear communication, consisten"},{"status":200,"guess":"unsure","confidence":0.0138,"model_score":0.4815,"style_score":0.6272,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The committee reviewed the available options and agreed that a phased "},{"status":200,"guess":"ai","confidence":0.3004,"model_score":0.7602,"style_score":0.7097,"label":"We think this was probably written by an AI system.","sent":"To configure the service, edit the settings file in the installation d"},{"status":200,"guess":"unsure","confidence":0.0678,"model_score":0.634,"style_score":0.5762,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The importance of effective communication in the workplace cannot be o"}]
```

### Criterion 3 — all labels reachable

```json
[{"status":200,"guess":"ai","confidence":0.5246,"model_score":0.9729,"style_score":0.7805,"label":"We think this was probably written by an AI system.","sent":"The importance of effective communication in the workplace cannot be o"},{"status":200,"guess":"human","confidence":0.7166,"model_score":0.0,"style_score":0.3333,"label":"We think this was probably written by a person.","sent":"\u0000\u0001\u0002 test \u001b[31mred\u001b[0m"},{"status":200,"guess":"unsure","confidence":0.0138,"model_score":0.4815,"style_score":0.6272,"label":"We cannot confidently determine whether this was written by a person or generated by AI.","sent":"The committee reviewed the available options and agreed that a phased "}]
```

### Criterion 4 — appeal path

```json
[{"status":200,"guess":"human","confidence":0.3646,"model_score":0.1212,"style_score":0.6667,"label":"We think this was probably written by a person.","sent":"I wrote this short submission myself and want the service to record my","appeal":{"status":200,"payload":{"content_id":"f0467e91-ecd0-472b-9b1c-fa516c5ccea5","message":"Your appeal has been recorded for review.","status":"under_review"},"content_id":"f0467e91-ecd0-472b-9b1c-fa516c5ccea5"}},{"status":200,"guess":"human","confidence":0.4924,"model_score":0.0375,"style_score":0.6506,"label":"We think this was probably written by a person.","sent":"This second submission is intentionally ordinary, so the appeal test c","appeal":{"status":200,"payload":{"content_id":"9adf1c72-2d61-40c6-80dd-fed8246e4723","message":"Your appeal has been recorded for review.","status":"under_review"},"content_id":"9adf1c72-2d61-40c6-80dd-fed8246e4723"},"unknown_appeal":{"status":404,"payload":{"error":"not_found","message":"No submission exists for this content_id."}}}]
```

### Criterion 5 — bad input

```json
[{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"(no JSON body)"},{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"{}"},{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"{\"creator_id\": \"eval_bad_missing\"}"},{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"(empty text)"},{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"   \t\n"},{"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"},{"status":413,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"word word word word word word word word word word word word word word "}]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

### Criterion verdicts

- **Criterion 1 — MET.** All three trials classified `0/10` of my own
  samples as high-confidence AI, meeting the target of at most `1/10`.
- **Criterion 2 — MISSED.** The human mean was `0.427` and the AI mean was
  `0.547`, a gap of only `0.121` rather than the required `0.20`. Four of
  five AI samples were above `0.50`, but the mean-gap requirement still failed
  in all three identical trials. The stage is the **combining rule**: the
  weighted model/style/lexical average compresses these groups into the
  unsure band instead of preserving enough separation. The mechanism is that
  the model and style signals disagree or remain moderate on formal text, and
  the weights (`0.50/0.35/0.15`) produce combined scores near the middle.
- **Criterion 3 — MET.** The three submissions reached `ai`, `human`, and
  `unsure` in every trial, and each reader-facing label matched its score
  band.
- **Criterion 4 — MET.** Both known-content appeals returned `200` with
  `under_review`, and the unknown ID returned `404`. The log contained the
  appeal event and reasoning.
- **Criterion 5 — MET.** The no-body, missing-field, empty, whitespace,
  non-string, and oversized requests returned the required `400`/`413`
  responses without normal decisions.

### Broken attack diagnoses by pattern

The attack run had 27 broken cases. These are grouped by mechanism; each group
names every affected attack ID.

- **Signal two — text-shape manipulation:** EV01, EV02, EV03, EV06, and EV07
  all changed punctuation, sentence boundaries, quotations, or typo/word
  variety in AI-like text. The style signal measures sentence-length spread,
  vocabulary repetition, and punctuation density rather than authorship, so
  those edits made generated text look more varied or human-like. The
  **combining rule** then weighted that style score at `0.35`, pulling the
  combined score into `human` or `unsure`. This is one signal-two blind spot,
  not five unrelated route failures.
- **Signal one — predictability blind spots:** EV04 used unusual words and
  EV08 placed text below the detector's useful token window. Unusual wording
  raised perplexity, while short/window-limited input gave the local model
  too little context. The **model signal** therefore under-read the AI
  source; the combining rule received a misleading low model score and the
  label mapping produced `unsure` or `human`.
- **Both signals plus the combining rule:** EV05 used a heavy human-editing
  pass and EV09 bolted a human opening onto AI text. Those changes altered
  both predictability and surface style, so both imperfect signals moved
  downward. The **combining rule** averaged the weakened evidence and the
  **label mapping** consequently returned `human` or `unsure` instead of AI.
- **False positives at the label boundary:** FP05 and FP07 were genuine human
  writing but received combined scores `0.6622` and `0.6546`, just above the
  AI threshold of `0.65`. The **model signal** found technical/formulaic or
  deliberately repetitive language predictable, and the **style signal**
  found its regular vocabulary/punctuation machine-like. The **combining
  rule** preserved both high scores, and the **label mapping** turned a
  borderline result into the high-confidence-AI accusation rather than
  `unsure`.
- **Malformed input reaching the detector:** MF02 returned HTTP 500 for a
  single-character text. The stage is the **route/signal-one boundary**:
  route validation allowed the non-empty string through, then the model
  signal could not handle the too-short input and the unhandled exception
  produced a 500. MF03 and MF04 likewise passed control-character and
  punctuation-only text through the **route**, which did not reject
  semantically unusable text; the model and style signals then manufactured
  `human` scores from those inputs. MF05, MF06, and MF07 passed a very long
  token, emoji-only text, and right-to-left text through the route; the
  **signals** interpreted unusual tokenization/Unicode shapes as strong
  evidence and the **label mapping** emitted `ai`. These are validation
  failures first: the route should reject unsupported or non-linguistic
  content before either signal runs.
- **Flood acceptance before the limit:** FL01_01 through FL01_10 were accepted
  before FL01_11 and FL01_12 received `429`. The stage is the **route's rate
  limiting** layer, not either detector signal. The mechanism is the selected
  `10 per minute` policy: the first ten requests fit inside the configured
  bucket, so a 20-request burst can still create ten decisions before the
  limiter rejects the remainder. The limiter held the final two, but the
  attack goal was not fully prevented.

The dominant pattern is that the detector treats surface form as evidence of
authorship. The next improvement should therefore address input validation and
the signal/threshold calibration together: reject unusable text at the route,
and widen the unsure protection around the AI boundary rather than letting
technical human prose become an AI accusation. Criterion 2's miss is evidence
that the current weighted scores also do not separate formal human and AI
writing enough to justify confident labels.



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
