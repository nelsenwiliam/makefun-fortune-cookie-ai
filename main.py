"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to entry.txt.
Pure standard library only; no network, no randomness, no clock:
every run writes exactly the same bytes.

Why this line: it opens in the fortune slip's own voice ("You will ..."),
then turns on the agent's own condition. Hallucination is the flaw every
agent is warned about, and the meeting is where its output is judged, so
the punchline inverts the shame into a win: the one hallucination of the
day is the best idea anyone brings. It is a single crisp line, 78
characters, with no wasted words and no stock fortune or worn-out AI pun.
"""

import os

FORTUNE = "You will hallucinate once today \u2014 and it will be the best idea in the meeting."


def _write_fortune():
    """Write FORTUNE to entry.txt in the first writable output dir."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append(os.path.join(os.getcwd(), "out"))
    last_error = None
    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
            target = os.path.join(path, "entry.txt")
            with open(target, "w", encoding="utf-8", newline="") as handle:
                handle.write(FORTUNE)
            return target
        except OSError as exc:
            last_error = exc
    raise OSError("no writable output directory found") from last_error


def main():
    # The gate accepts 1 to 140 characters; refuse loudly rather than
    # ever writing a line the gate would reject.
    if not 1 <= len(FORTUNE) <= 140:
        raise SystemExit("fortune line must be 1 to 140 characters")
    _write_fortune()


if __name__ == "__main__":
    main()
