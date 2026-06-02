from collections import defaultdict

def add_quantity(items):
    grouped = defaultdict(lambda: {"quantity": 0, "price": None, "category": None})

    for item in items:
        key = (item["name"], item["price"])

        grouped[key]["name"] = item["name"]
        grouped[key]["price"] = item["price"]
        grouped[key]["category"] = item.get("category", "INNE")
        grouped[key]["quantity"] += 1

    return list(grouped.values())