from app.ocr.extractor import extract_text

from app.extraction.invoice_fields import (
    extract_invoice_data
)

from app.validation.invoice_validator import (
    validate_total,
    calculate_tax_percentage
)


# Invoice image
invoice_path = "data/invoices/sample.png"


# Step 1: OCR
print("Reading invoice...")

text = extract_text(invoice_path)


# Step 2: Extract fields
invoice_data = extract_invoice_data(text)


print("\n========== INVOICE DATA ==========\n")

for key, value in invoice_data.items():
    print(f"{key}: {value}")


# Step 3: Validate invoice
validation = validate_total(
    invoice_data
)


# Step 4: Calculate GST percentage
tax_percentage = calculate_tax_percentage(
    invoice_data
)


print("\n========== VALIDATION ==========\n")

print(
    f"Status: {validation['status']}"
)

if "expected_total" in validation:

    print(
        f"Expected Total: "
        f"{validation['expected_total']}"
    )

    print(
        f"Invoice Total: "
        f"{validation['invoice_total']}"
    )

    print(
        f"Difference: "
        f"{validation['difference']}"
    )


print(
    f"GST Percentage: "
    f"{tax_percentage}%"
)