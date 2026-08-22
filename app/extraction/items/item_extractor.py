import re


def extract_line_items(text):

    items = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    start_processing = False

    for line in lines:

        # Start reading after table header
        if (
            "Item" in line
            and "Quantity" in line
            and "Amount" in line
        ):
            start_processing = True
            continue

        # Stop when financial summary starts
        if line.lower().startswith(
            ("subtotal", "gst", "tax", "total")
        ):
            break

        if not start_processing:
            continue

        # Match:
        # Laptop 2 100000
        match = re.match(
            r"^(.+?)\s+(\d+)\s+([\d,]+(?:\.\d+)?)$",
            line
        )

        if match:

            item_name = match.group(1).strip()

            quantity = int(
                match.group(2)
            )

            amount = float(
                match.group(3).replace(",", "")
            )

            unit_price = (
                amount / quantity
                if quantity != 0
                else 0
            )

            items.append({
                "item": item_name,
                "quantity": quantity,
                "unit_price": round(
                    unit_price,
                    2
                ),
                "amount": amount
            })

    return items