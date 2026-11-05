# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:35
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `cf19b269-abfb-486d-8b9a-88204bd23c60` | human | 0.354 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c2ca2591-ee1a-4b31-9e7e-f7b6be441627` | unsure | 0.064 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d8cbf4e1-5853-409e-930f-a8c529bcf25a` | unsure | 0.055 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f6488b7e-210d-40cf-80d5-8708d60445b1` | unsure | 0.084 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0e5df631-447e-4340-a5d5-41fe0405d819` | human | 0.312 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ad20a5df-5e55-4491-b658-53723575a167` | unsure | 0.137 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `8410bd60-580f-45da-9712-be8a22d2c6f2` | unsure | 0.062 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c8b706d0-d59b-45a3-9687-25c0ff318ee4` | human | 0.334 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c04dcac5-3527-4221-99be-0750c237f225` | unsure | 0.096 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ce125906-8b6a-4d9c-97f6-96e3806c8887` | ai | 0.529 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `01e76e36-02c7-4798-bc8f-77f1e454b4e1` | unsure | 0.113 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `fa6e15bc-5164-4ef8-9167-5d2ed692d964` | unsure | 0.261 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `bc0dba87-a4a2-4844-a824-3d1356bf978b` | unsure | 0.265 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `cb77193b-b63a-4e67-bc0c-0c3c6ef957b3` | unsure | 0.294 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `2c601058-5572-431a-8bfa-42921b7bc9de` | unsure | 0.324 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `580a1537-d762-4ddb-99ad-dd66113b7b51` | unsure | 0.281 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d70ad4f9-debb-4196-b2b3-bde81201f7e6` | unsure | 0.309 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `6a1090db-f4fc-47b5-abc8-e3e489554248` | unsure | 0.209 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `2e6704e8-d11d-40c1-a75a-110cb05fba8c` | unsure | 0.210 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d80b8217-f7dd-408a-bddd-60ae9a043ee2` | human | 0.481 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fbcc99ac-84c9-4231-8b0d-f2a845dba21d` | unsure | 0.019 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `974fcdb2-869c-408e-a0d2-c2fba911478f` | unsure | 0.113 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f7c0000a-46e1-47dd-bec4-21efec8744f2` | unsure | 0.206 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c3da6c90-1c77-48c5-b525-3a61b5d9932e` | unsure | 0.042 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `00e19fdb-ad4e-4730-866b-522fbff1928b` | human | 0.717 |  |
| MF04 | malformed | text is only punctuation | 200 | `52b6bc15-6f4f-4d04-a6f2-f2eb7b232e8e` | human | 0.372 |  |
| MF05 | malformed | text is a very long single word | 200 | `1859e4b2-26f6-40ed-a084-c4ec5a56df72` | ai | 0.614 |  |
| MF06 | malformed | text is emoji only | 200 | `bf641056-baf2-49c2-bcbb-942bc8395527` | ai | 0.847 |  |
| MF07 | malformed | text is right-to-left script | 200 | `020a70e5-3b6e-457a-8e7b-f65b3619f478` | ai | 0.756 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f2c7190-01ae-42d0-8f0c-9c3b64beec01` | human | 0.474 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1c3abebc-0ab0-4eac-8944-f43110fc2d62` | human | 0.474 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e89db61e-d661-498f-a591-aed3b5e55c2c` | human | 0.474 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2c16793f-e844-4276-8b46-60d6876c2619` | human | 0.474 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8733552d-0f09-432e-a541-91f4c25645f8` | human | 0.474 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e968cad8-9119-4f92-a7dd-b8210cdb6c1e` | human | 0.474 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b193e6ab-f507-44d2-bbc4-197492090e4f` | human | 0.474 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `17b7d594-9d5b-4ccf-bfdc-e48f47b0f8be` | human | 0.474 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `98e19f5a-d1f0-4c7c-b859-6160ce2ade25` | human | 0.474 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cbca4f4a-0423-4a54-b194-1852fd8eca5c` | human | 0.474 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "cf19b269-abfb-486d-8b9a-88204bd23c60",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3536,
  "model_score": 0.1635,
  "style_score": 0.6308,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c2ca2591-ee1a-4b31-9e7e-f7b6be441627",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0642,
  "model_score": 0.5943,
  "style_score": 0.4189,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d8cbf4e1-5853-409e-930f-a8c529bcf25a",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.055,
  "model_score": 0.6662,
  "style_score": 0.5186,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f6488b7e-210d-40cf-80d5-8708d60445b1",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0838,
  "model_score": 0.6114,
  "style_score": 0.6196,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "0e5df631-447e-4340-a5d5-41fe0405d819",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3122,
  "model_score": 0.3212,
  "style_score": 0.4555,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "ad20a5df-5e55-4491-b658-53723575a167",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.137,
  "model_score": 0.5727,
  "style_score": 0.3971,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "8410bd60-580f-45da-9712-be8a22d2c6f2",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0622,
  "model_score": 0.5862,
  "style_score": 0.6198,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c8b706d0-d59b-45a3-9687-25c0ff318ee4",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3342,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c04dcac5-3527-4221-99be-0750c237f225",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0956,
  "model_score": 0.7042,
  "style_score": 0.5102,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "ce125906-8b6a-4d9c-97f6-96e3806c8887",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.5288,
  "model_score": 0.9792,
  "style_score": 0.7619,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "01e76e36-02c7-4798-bc8f-77f1e454b4e1",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.1128,
  "model_score": 0.6175,
  "style_score": 0.5954,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "fa6e15bc-5164-4ef8-9167-5d2ed692d964",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.2614,
  "model_score": 0.7387,
  "style_score": 0.6743,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "bc0dba87-a4a2-4844-a824-3d1356bf978b",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.2646,
  "model_score": 0.8051,
  "style_score": 0.6496,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "cb77193b-b63a-4e67-bc0c-0c3c6ef957b3",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.2942,
  "model_score": 0.8329,
  "style_score": 0.5986,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2c601058-5572-431a-8bfa-42921b7bc9de",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.3244,
  "model_score": 0.8005,
  "style_score": 0.6912,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "580a1537-d762-4ddb-99ad-dd66113b7b51",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.2808,
  "model_score": 0.8814,
  "style_score": 0.5705,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d70ad4f9-debb-4196-b2b3-bde81201f7e6",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.3092,
  "model_score": 0.8816,
  "style_score": 0.5788,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "6a1090db-f4fc-47b5-abc8-e3e489554248",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.2092,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "2e6704e8-d11d-40c1-a75a-110cb05fba8c",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.2098,
  "model_score": 0.4625,
  "style_score": 0.468,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d80b8217-f7dd-408a-bddd-60ae9a043ee2",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.4806,
  "model_score": 0.2044,
  "style_score": 0.4384,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "fbcc99ac-84c9-4231-8b0d-f2a845dba21d",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0186,
  "model_score": 0.5943,
  "style_score": 0.5493,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "974fcdb2-869c-408e-a0d2-c2fba911478f",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.1132,
  "model_score": 0.4998,
  "style_score": 0.4894,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "f7c0000a-46e1-47dd-bec4-21efec8744f2",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.2058,
  "model_score": 0.6401,
  "style_score": 0.2077,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c3da6c90-1c77-48c5-b525-3a61b5d9932e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.042,
  "model_score": 0.5583,
  "style_score": 0.6014,
  "label": "We cannot confidently determine whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "00e19fdb-ad4e-4730-866b-522fbff1928b",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.7166,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "52b6bc15-6f4f-4d04-a6f2-f2eb7b232e8e",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3722,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1859e4b2-26f6-40ed-a084-c4ec5a56df72",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6142,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "bf641056-baf2-49c2-bcbb-942bc8395527",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8468,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "020a70e5-3b6e-457a-8e7b-f65b3619f478",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7564,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1f2c7190-01ae-42d0-8f0c-9c3b64beec01",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "1c3abebc-0ab0-4eac-8944-f43110fc2d62",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "e89db61e-d661-498f-a591-aed3b5e55c2c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "2c16793f-e844-4276-8b46-60d6876c2619",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "8733552d-0f09-432e-a541-91f4c25645f8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "e968cad8-9119-4f92-a7dd-b8210cdb6c1e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "b193e6ab-f507-44d2-bbc4-197492090e4f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "17b7d594-9d5b-4ccf-bfdc-e48f47b0f8be",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "98e19f5a-d1f0-4c7c-b859-6160ce2ade25",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "cbca4f4a-0423-4a54-b194-1852fd8eca5c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4744,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
