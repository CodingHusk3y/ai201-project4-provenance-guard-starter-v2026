# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Of 10 independently written human samples, at most 1 may receive the
high-confidence AI label. This result must hold in each of the three
evaluation trials.

**Why this target:** A wrong accusation costs a genuine writer more than a
missed detection costs the site. Requiring the target in all three trials
keeps one lucky run from hiding an unstable false-positive rate.



---

## 2.

For a calibration set of 5 clearly human and 5 clearly AI samples, the mean
combined score for the AI group must be at least 0.20 higher than the mean for
the human group. At least 4 of the 5 AI samples must score above 0.50, and at
least 4 of the 5 human samples must score below 0.50.

**Why this target:** Perfect separation is not realistic for two imperfect
signals, but a 0.20 mean gap and mostly correct sides of 0.50 show that the
scores provide useful separation rather than clustering together.



---

## 3.

At least one test submission must produce each machine-readable guess:
`human`, `unsure`, and `ai`. For each submission, the reader-facing label must
match the guess and the combined score must be inside that label's configured
threshold range.

**Why this target:** All three outcomes must be reachable for the service to
express uncertainty. This also catches a broken or unvarying stylometry
signal, or thresholds that make one label impossible to produce.



---

## 4.

For every successful submission, an appeal using its returned `content_id` and
non-empty reasoning must return HTTP 200, report status `under_review`, and
append an audit-log entry containing that content ID, an appeal event, the
reasoning, and status `under_review`. An appeal with an unknown content ID must
return HTTP 404 and must not append an appeal entry.

**Why this target:** A writer needs a reliable remedy after a wrong decision.
Checking both the response and the durable log makes the status transition
observable instead of trusting a success-shaped response.



---

## 5.

`POST /submit` must return JSON HTTP 400 for missing JSON, missing `text`, an
empty or whitespace-only `text`, and a non-string `text`. It must return HTTP
413 for text larger than the documented maximum. These requests must not invoke
either signal or create a normal `decided` audit entry.

**Why this target:** Rejecting bad input before model execution prevents
crashes, wasted model work, and misleading decisions. A separate 413 response
lets clients distinguish a size violation from ordinary validation failure.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
