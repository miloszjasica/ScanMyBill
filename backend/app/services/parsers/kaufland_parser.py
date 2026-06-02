import re

PRICE_RE = re.compile(r"^\d+[.,]\d{2}$")

PRICE_IN_LINE = re.compile(r"(\d+[.,]\d{2})")

def extract_price(line):
    match = PRICE_IN_LINE.search(line)
    if match:
        return float(match.group(1).replace(",", "."))
    return None


def parse_kaufland(raw_text: str):

    data = {
        "store": "Kaufland",
        "date": None,
        "items": [],
        "total": None
    }

    lines = [
        line.strip()
        for line in raw_text.splitlines()
        if line.strip()
    ]

    i = 0

    while i < len(lines):

        line = lines[i]

        lower = line.lower()

        if "ogółem" in lower or "ogotem" in lower or "og0tem" in lower:

            if i + 1 < len(lines):

                price = lines[i + 1]

                if PRICE_RE.match(price):
                    data["total"] = float(price.replace(",", "."))

            break

        if i + 1 < len(lines):

            next_line = lines[i + 1]

            price = extract_price(next_line)

            if price is not None:
                data["items"].append({
                    "name": line,
                    "price": price
    })

                i += 2
                continue

        i += 1

    return data