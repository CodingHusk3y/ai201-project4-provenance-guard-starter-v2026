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

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



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

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** The final score is a weighted average of the two scores. The
signals point in the same direction, so a higher result always means more
AI-like. Disagreement is retained as uncertainty in the middle rather than
allowing either signal to override the other.

**The numbers:** `0.50 * model_score + 0.50 * style_score`, rounded to four
decimal places and clamped to the 0.0–1.0 range. The weights come from
`config.WEIGHT_MODEL_SIGNAL` and `config.WEIGHT_STYLE_SIGNAL`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** The
clearly human sample in the calibration run produced a model score of `0.5844`
and a style score of `0.4831`. The model leaned AI-like while stylometry
leaned more human-like; the weighted average preserves that disagreement
instead of making either signal decisive on its own.

**Calibration run (same text passed to both signals):**

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
{"combined_score":0.628,"confidence":0.256,"content_id":"3de55966-615a-428c-b7f5-7bd8a963d749","guess":"unsure","label":"We cannot confidently determine whether this was written by a person or generated by AI.","model_score":0.6987,"style_score":0.5574}
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

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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
