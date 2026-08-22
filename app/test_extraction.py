from app.ocr.extractor import extract_text

from app.extraction.invoice_fields import (
    extract_invoice_data
)


invoice_path = "data/invoices/sample.png"


print("Reading invoice...")

text = extract_text(invoice_path)


print("\n========== RAW OCR TEXT ==========\n")

print(text)


invoice_data = extract_invoice_data(text)


print("\n========== EXTRACTED DATA ==========\n")


for key, value in invoice_data.items():

    print(
        f"{key}: {value}"
    )