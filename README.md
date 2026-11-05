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
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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
