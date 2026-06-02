def aggregate_quantity(items):
    grouped = {}

    for item in items:
        key = (item["name"], item["price"])

        if key not in grouped:
            grouped[key] = {
                "name": item["name"],
                "price": item["price"],
                "quantity": 1
            }
        else:
            grouped[key]["quantity"] += 1

    return list(grouped.values())