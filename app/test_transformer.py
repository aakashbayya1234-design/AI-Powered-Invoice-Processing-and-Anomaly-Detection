from app.ocr.extractor import extract_text

from app.transformer.invoice_classifier import (
    InvoiceTextClassifier
)


invoice_path = "data/invoices/sample.png"


print("\n========== READING INVOICE ==========\n")

text = extract_text(invoice_path)

print(text)


print("\n========== TRANSFORMER ==========\n")

classifier = InvoiceTextClassifier()

result = classifier.classify(text)


print("\n========== CLASSIFICATION ==========\n")

print(result)