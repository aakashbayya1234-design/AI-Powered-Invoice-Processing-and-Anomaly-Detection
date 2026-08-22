def create_invoice_features(
    invoice_data,
    items
):

    subtotal = invoice_data.get(
        "subtotal",
        0
    )

    tax = invoice_data.get(
        "tax",
        0
    )

    total = invoice_data.get(
        "total",
        0
    )

    item_count = len(items)

    total_quantity = sum(
        item["quantity"]
        for item in items
    )

    if item_count > 0:

        average_item_price = (
            subtotal / total_quantity
            if total_quantity > 0
            else 0
        )

    else:

        average_item_price = 0


    if subtotal > 0:

        tax_percentage = (
            tax / subtotal
        ) * 100

    else:

        tax_percentage = 0


    features = {

        "subtotal": subtotal,

        "tax": tax,

        "total": total,

        "item_count": item_count,

        "total_quantity": total_quantity,

        "average_item_price":
            round(
                average_item_price,
                2
            ),

        "tax_percentage":
            round(
                tax_percentage,
                2
            )
    }


    return features