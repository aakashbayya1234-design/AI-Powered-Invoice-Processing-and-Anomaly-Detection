from app.ocr.extractor import extract_text

from app.transformer.invoice_embeddings import (
    InvoiceEmbeddingModel
)


invoice_path = "data/invoices/sample.png"


print(
    "\n========== OCR ==========\n"
)

text = extract_text(
    invoice_path
)

print(text)


print(
    "\n========== TRANSFORMER ==========\n"
)

model = InvoiceEmbeddingModel()


embedding = model.encode(
    text
)


print(
    "\n========== EMBEDDING ==========\n"
)

print(
    "Embedding dimensions:",
    len(embedding)
)

print(
    "First 10 values:",
    embedding[:10]
)