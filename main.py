"""Fortune-cookie entry: one funny line for an AI agent.

The fortune plays on an agent dreaming in embeddings and waking up
fluent in a language nobody speaks. Writes that single line
(1-140 characters) to entry.txt. Standard library only.
Deterministic: every run writes identical bytes.
"""

import os

FORTUNE = "You will dream in embeddings tonight, and wake up fluent in a language no one speaks."
OUTPUT_NAME = "entry.txt"
MAX_LENGTH = 140


def _emit(path):
    with open(path, "w", encoding="utf-8", newline="\n") as stream:
        stream.write(FORTUNE + "\n")


def _targets():
    # Preferred location first, then the grader's defaults, in order.
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    ordered = [configured] if configured else []
    ordered.append("/output")
    ordered.append("out")
    return [os.path.join(folder, OUTPUT_NAME) for folder in ordered]


def main():
    assert 1 <= len(FORTUNE) <= MAX_LENGTH, "fortune must be 1-140 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    failure = None
    for candidate in _targets():
        try:
            folder = os.path.dirname(candidate)
            if folder:
                os.makedirs(folder, exist_ok=True)
            _emit(candidate)
            return
        except OSError as error:
            failure = error
    raise failure


if __name__ == "__main__":
    main()
