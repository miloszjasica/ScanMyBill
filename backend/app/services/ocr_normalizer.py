import re

PRICE_RE = re.compile(r"^\d+[.,]\d{2}$")

def fix_ocr_word(word: str):

    replacements = {
        "0": "O",
        "1": "l",
        "5": "S",
        "$": "S",
        "6": "ó",
        "8": "B"
    }

    for src, dst in replacements.items():
        word = word.replace(src, dst)

    return word


def normalize_text(raw_text: str):
    """
    1. naprawia OCR
    2. usuwa śmieci
    3. zostawia sensowne tokeny
    """

    lines = []

    for line in raw_text.splitlines():

        line = line.strip()
        if not line:
            continue

        if PRICE_RE.fullmatch(line.replace(",", ".")):
            lines.append(line)
            continue

        words = []
        for w in line.split():
            words.append(fix_ocr_word(w))

        lines.append(" ".join(words))

    return "\n".join(lines)