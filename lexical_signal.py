"""
Signal three: lexical rhythm.

This signal looks at variation in word length, which is different from the
sentence-level and vocabulary measures in stylometry.py. Generated prose often
uses words of similar length; human writing tends to mix short and long words.
"""

import statistics

from stylometry import words


def lexical_signal(text: str) -> float:
    """Return a 0–1 AI-likelihood score based on word-length variation."""
    lengths = [len(word) for word in words(text)]
    if len(lengths) < 2:
        return 0.5

    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.5

    variation = statistics.stdev(lengths) / mean
    human_likelihood = min(variation / 0.6, 1.0)
    return round(1.0 - human_likelihood, 4)
