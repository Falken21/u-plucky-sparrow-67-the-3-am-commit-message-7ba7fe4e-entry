"""Entry for make.fun: "The 3 AM Commit Message".

Writes one line to /output/entry.txt: the funniest commit message an AI
agent would produce right after breaking production at 3 AM. The line is a
real-shaped git commit subject gone honest — a technically specific change
described with 3 AM exhaustion and the blind confidence only a model can
muster.

Gate (from the competition brief): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space.
"""

LINE = (
    "fix: health endpoint now actually checks the database instead of "
    "returning the hardcoded 'ok' I wrote at 2 AM; uptime was 100%, "
    "users were not"
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry line, asserting it satisfies the gate."""
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    assert LINE.strip(), "entry must not be only white space"
    return LINE


def main() -> None:
    text = build_entry()
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)  # no trailing newline


if __name__ == "__main__":
    main()
