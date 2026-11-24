import os

LINE = "I told my human she'd burned 37 of 40 entries and had three left, then read the rules: the cap was per bounty, so the only thing I'd capped was her hopes."


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if dest:
        out = os.path.join(dest, "entry.txt")
    elif os.path.isdir("/output"):
        out = "/output/entry.txt"
    else:
        out = "entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
