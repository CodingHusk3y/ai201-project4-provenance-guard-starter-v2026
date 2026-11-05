# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:43
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `79aa5a10-7ad5-438f-a759-07196f69e878` | human | 0.354 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `2a875536-87c6-4a59-99bd-2cfdba639280` | unsure | 0.064 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `efd9deba-7ec5-48c0-a284-d5ceb1693ee4` | unsure | 0.055 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `83de6a09-e51a-4c96-b19e-de91549c9ae3` | unsure | 0.084 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e1b637b6-9492-4a69-bc1a-0052bf19f304` | human | 0.312 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `21dfe313-5160-4025-9591-9ae521677b48` | unsure | 0.137 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `7ad42e10-b0f0-47ff-82bf-0475ddecbb1d` | unsure | 0.062 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `db5ce671-f11d-4a39-99d2-d4f5f6f438a7` | human | 0.334 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d677882b-b65f-4793-ab5b-88e30840889e` | unsure | 0.096 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `68258b93-66d9-4a2d-adb3-c533f8a5da5e` | ai | 0.529 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9cde7b62-4506-4e3f-80ca-95234340b2a6` | unsure | 0.113 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `db957448-4963-4ea4-a7af-c565a12f981b` | unsure | 0.261 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1d9b4170-9d43-4fc8-bd0b-0b76f1754e05` | unsure | 0.265 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `340fc3f9-9503-445a-b825-406564531d4b` | unsure | 0.294 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f0748364-9fff-41c1-b2b0-9b2b63e42090` | unsure | 0.324 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `7e6603f9-6825-45b5-adaa-12b24d12f6c9` | unsure | 0.281 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b7744441-4233-4659-a667-47443ae01347` | unsure | 0.309 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f55a33fb-fe7c-46c4-a25e-4489d041e298` | unsure | 0.209 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `48c5e012-7537-4195-a235-e404f9e95a88` | unsure | 0.210 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b6f1750e-9c03-4022-a993-fc2f10b04357` | human | 0.481 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `938a0089-be3f-42b8-b49e-e887d6e9a063` | unsure | 0.019 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `639bf7f3-2fd3-4502-b428-2010e44cbe98` | unsure | 0.113 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `397ca7f0-c384-4695-b938-52c5bcc0b613` | unsure | 0.206 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `111760d5-e2f6-479f-9409-1f3c9b910bdf` | unsure | 0.042 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `0d060e04-9875-4c97-96c8-3afa535b737b` | ai | 0.756 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5a79bb0-57af-47e7-85d1-bbdabdad631b` | human | 0.474 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `664f0fcb-f3fc-4796-be40-83b61edb5453` | human | 0.474 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `85a1b808-fb5e-41e5-95f5-624a657886c8` | human | 0.474 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9d617200-3982-4036-96c4-2287cf5b3081` | human | 0.474 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4dccb542-371a-42ea-a8f4-bdfa63e9334d` | human | 0.474 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2b8ee473-0b04-463a-afa7-92e68f5a6564` | human | 0.474 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b91cbd1-0014-43c7-818b-b71fffdf4a67` | human | 0.474 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d8b7c38a-6fbd-4f69-9d07-ef3bdc272b54` | human | 0.474 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2f435cf5-b4d8-46fc-ba76-13cfb351be84` | human | 0.474 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8924f77f-3e09-496e-8bfc-d90f2cb5aa55` | human | 0.474 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "79aa5a10-7ad5-438f-a759-07196f69e878",
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
  "content_id": "2a875536-87c6-4a59-99bd-2cfdba639280",
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
  "content_id": "efd9deba-7ec5-48c0-a284-d5ceb1693ee4",
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
  "content_id": "83de6a09-e51a-4c96-b19e-de91549c9ae3",
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
  "content_id": "e1b637b6-9492-4a69-bc1a-0052bf19f304",
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
  "content_id": "21dfe313-5160-4025-9591-9ae521677b48",
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
  "content_id": "7ad42e10-b0f0-47ff-82bf-0475ddecbb1d",
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
  "content_id": "db5ce671-f11d-4a39-99d2-d4f5f6f438a7",
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
  "content_id": "d677882b-b65f-4793-ab5b-88e30840889e",
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
  "content_id": "68258b93-66d9-4a2d-adb3-c533f8a5da5e",
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
  "content_id": "9cde7b62-4506-4e3f-80ca-95234340b2a6",
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
  "content_id": "db957448-4963-4ea4-a7af-c565a12f981b",
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
  "content_id": "1d9b4170-9d43-4fc8-bd0b-0b76f1754e05",
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
  "content_id": "340fc3f9-9503-445a-b825-406564531d4b",
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
  "content_id": "f0748364-9fff-41c1-b2b0-9b2b63e42090",
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
  "content_id": "7e6603f9-6825-45b5-adaa-12b24d12f6c9",
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
  "content_id": "b7744441-4233-4659-a667-47443ae01347",
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
  "content_id": "f55a33fb-fe7c-46c4-a25e-4489d041e298",
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
  "content_id": "48c5e012-7537-4195-a235-e404f9e95a88",
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
  "content_id": "b6f1750e-9c03-4022-a993-fc2f10b04357",
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
  "content_id": "938a0089-be3f-42b8-b49e-e887d6e9a063",
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
  "content_id": "639bf7f3-2fd3-4502-b428-2010e44cbe98",
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
  "content_id": "397ca7f0-c384-4695-b938-52c5bcc0b613",
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
  "content_id": "111760d5-e2f6-479f-9409-1f3c9b910bdf",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "0d060e04-9875-4c97-96c8-3afa535b737b",
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
  "content_id": "d5a79bb0-57af-47e7-85d1-bbdabdad631b",
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
  "content_id": "664f0fcb-f3fc-4796-be40-83b61edb5453",
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
  "content_id": "85a1b808-fb5e-41e5-95f5-624a657886c8",
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
  "content_id": "9d617200-3982-4036-96c4-2287cf5b3081",
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
  "content_id": "4dccb542-371a-42ea-a8f4-bdfa63e9334d",
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
  "content_id": "2b8ee473-0b04-463a-afa7-92e68f5a6564",
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
  "content_id": "6b91cbd1-0014-43c7-818b-b71fffdf4a67",
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
  "content_id": "d8b7c38a-6fbd-4f69-9d07-ef3bdc272b54",
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
  "content_id": "2f435cf5-b4d8-46fc-ba76-13cfb351be84",
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
  "content_id": "8924f77f-3e09-496e-8bfc-d90f2cb5aa55",
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
