"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I keep a short list of tasks beside my keyboard because the list helps me notice what I am actually choosing to do. When a task changes, I cross it out and write the new version rather than pretending the first plan was still right.",
            "The bus was late again, so I walked the last six blocks with my coffee cooling in my hand. I arrived annoyed, then noticed the bakery had put its day-old bread outside and came home with a loaf I had not planned to buy.",
            "I learned to repair small things from my grandfather. He never started with a manual; he turned the object over, tapped the loose part, and asked what had changed since yesterday.",
            "My first draft of the volunteer schedule was too tidy to use. People had different commutes and one person needed to leave early, so I moved the names around until the gaps were visible.",
            "I prefer a notebook to a new productivity app for ideas that are not ready yet. Paper lets me leave a sentence unfinished, which is sometimes the most honest description of where the thought is.",
            "At the farmers market I bought tomatoes because they smelled good, not because dinner required them. That small decision made the rest of the meal easier: rice, tomatoes, and whatever herbs were still alive in the window box.",
            "The room looked clean until I tried to find the charger. I emptied one drawer onto the floor, sorted the cables by length, and discovered three things I had been looking for since winter.",
            "I used to save every receipt in one envelope. It felt responsible, but it made the envelope impossible to use, so now I keep only the receipts I might actually need and recycle the rest each Friday.",
            "When the rain started, our dog refused the usual route and pulled toward the park. We took the longer path, got soaked, and found a duckling pond that neither of us had noticed before.",
            "I rewrote the note twice because the first version sounded certain and the second sounded apologetic. The third version simply said what I needed and left room for the other person to answer.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Five personal samples form the human group; the formal samples form
        # the clearly machine-like group used for score separation.
        "texts": [
            "The bus was late again, so I walked the last six blocks with my coffee cooling in my hand. I arrived annoyed, then noticed the bakery had put its day-old bread outside and came home with a loaf I had not planned to buy.",
            "I learned to repair small things from my grandfather. He never started with a manual; he turned the object over, tapped the loose part, and asked what had changed since yesterday.",
            "My first draft of the volunteer schedule was too tidy to use. People had different commutes and one person needed to leave early, so I moved the names around until the gaps were visible.",
            "At the farmers market I bought tomatoes because they smelled good, not because dinner required them. That small decision made the rest of the meal easier: rice, tomatoes, and whatever herbs were still alive in the window box.",
            "I rewrote the note twice because the first version sounded certain and the second sounded apologetic. The third version simply said what I needed and left room for the other person to answer.",
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must support diverse inputs. Additionally, overall performance depends on multiple variables.",
            "A successful organization benefits from clear communication, consistent processes, and measurable objectives. By aligning resources with strategic priorities, teams can improve efficiency while maintaining the flexibility required to respond to changing conditions.",
            "The committee reviewed the available options and agreed that a phased approach would reduce risk. Each stage will have a defined owner, a short review period, and a documented decision before the next stage begins.",
            "To configure the service, edit the settings file in the installation directory. Set the host value to the address the service should bind to. Set the port value to an unused port above 1024. Save the file and restart the service.",
            "The importance of effective communication in the workplace cannot be overstated. Teams that communicate clearly are better positioned to achieve their objectives and avoid costly misunderstandings. Three strategies improve performance: regular check-ins, documented decisions, and an environment where questions are welcomed.",
        ],
    },
    {
        "name": "all labels reachable",
        "criterion": 3,
        # The repeated formal passage is high-score, the short personal note
        # is low-score, and the ordinary mixed passage should remain unsure.
        "texts": [
            "The importance of effective communication in the workplace cannot be overstated. Teams that communicate clearly are better positioned to achieve their objectives and avoid costly misunderstandings. The importance of effective communication in the workplace cannot be overstated. Teams that communicate clearly are better positioned to achieve their objectives and avoid costly misunderstandings.",
            "I made tea.",
            "The committee reviewed the available options and agreed that a phased approach would reduce risk. Each stage will have a defined owner, a short review period, and a documented decision before the next stage begins.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeal": True,
        "texts": [
            "I wrote this short submission myself and want the service to record my request for review.",
            "This second submission is intentionally ordinary, so the appeal test checks the workflow rather than a particular label.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            None,
            {},
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \t\n", "creator_id": "eval_bad_whitespace"},
            {"text": 42, "creator_id": "eval_bad_number"},
            {"text": "word " * 2500, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if body is not None and not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
