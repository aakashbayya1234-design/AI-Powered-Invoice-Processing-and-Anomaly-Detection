def validate_total(invoice_data):

    subtotal = invoice_data.get("subtotal")
    tax = invoice_data.get("tax")
    total = invoice_data.get("total")

    if subtotal is None:
        return {
            "status": "ERROR",
            "message": "Subtotal is missing"
        }

    if tax is None:
        return {
            "status": "ERROR",
            "message": "Tax/GST is missing"
        }

    if total is None:
        return {
            "status": "ERROR",
            "message": "Total is missing"
        }

    expected_total = subtotal + tax

    difference = total - expected_total

    # Allow a tiny rounding difference
    tolerance = 1.0

    if abs(difference) <= tolerance:

        return {
            "status": "VALID",
            "expected_total": expected_total,
            "invoice_total": total,
            "difference": difference
        }

    return {
        "status": "ANOMALY",
        "expected_total": expected_total,
        "invoice_total": total,
        "difference": difference,
        "message": "Invoice total does not match subtotal + tax"
    }


def calculate_tax_percentage(invoice_data):

    subtotal = invoice_data.get("subtotal")
    tax = invoice_data.get("tax")

    if not subtotal or tax is None:
        return None

    percentage = (
        tax / subtotal
    ) * 100

    return round(percentage, 2)