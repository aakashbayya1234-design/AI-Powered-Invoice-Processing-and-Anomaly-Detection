import re


def clean_lines(text):
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


def extract_vendor(text):
    lines = clean_lines(text)

    for line in lines:
        if line.upper() in ["INVOICE", "TAX INVOICE"]:
            break

        return line

    return None


def extract_invoice_number(text):
    patterns = [
        r"Invoice\s+Number\s*[:\-]\s*([A-Z0-9\-]+)",
        r"Invoice\s+No\.?\s*[:\-]\s*([A-Z0-9\-]+)",
        r"Invoice\s+#\s*[:\-]?\s*([A-Z0-9\-]+)",
        r"Invoice\s+ID\s*[:\-]\s*([A-Z0-9\-]+)"
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return None


def extract_date(text, field_name):
    pattern = (
        rf"\b{field_name}\b"
        r"\s*[:\-]?\s*"
        r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})"
    )

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


def extract_amount(text, field_name):
    pattern = (
        rf"(?im)^\s*{field_name}"
        r"\s*[:\-]?\s*"
        r"[₹$]?\s*"
        r"([\d,]+(?:\.\d+)?)"
        r"\s*$"
    )

    match = re.search(
        pattern,
        text
    )

    if match:
        return float(
            match.group(1).replace(",", "")
        )

    return None


def extract_tax(text):
    pattern = (
        r"(?im)^\s*"
        r"(?:GST|Tax)"
        r"(?:\s*\(\d+(?:\.\d+)?%\))?"
        r"\s*[:\-]?\s*"
        r"[₹$]?\s*"
        r"([\d,]+(?:\.\d+)?)"
        r"\s*$"
    )

    match = re.search(
        pattern,
        text
    )

    if match:
        return float(
            match.group(1).replace(",", "")
        )

    return None


def extract_invoice_data(text):

    invoice_data = {
        "vendor": extract_vendor(text),

        "invoice_number": extract_invoice_number(text),

        "invoice_date": extract_date(
            text,
            "Invoice Date"
        ),

        "due_date": extract_date(
            text,
            "Due Date"
        ),

        "subtotal": extract_amount(
            text,
            "Subtotal"
        ),

        "tax": extract_tax(text),

        "total": extract_amount(
            text,
            "Total"
        )
    }

    return invoice_data