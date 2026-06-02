import re

PRICE_LINE = re.compile(
    r"(?P<name>.+?)\s+(?P<qty>\d+[.,]\d+|\d+)\s*\*\s*(?P<unit>\d+[.,]\d+)\s+(?P<total>\d+[.,]\d+)"
)


def to_float(x: str) -> float:
    return float(x.replace(",", "."))


def parse_lidl(lines: list[str]):
    items = []

    for line in lines:
        m = PRICE_LINE.search(line)
        if not m:
            continue

        name = m.group("name").strip()
        qty = to_float(m.group("qty"))
        unit = to_float(m.group("unit"))
        total = to_float(m.group("total"))

        items.append({
            "name": name,
            "price": total,
            "qty": qty,
            "unit_price": unit
        })

    return items