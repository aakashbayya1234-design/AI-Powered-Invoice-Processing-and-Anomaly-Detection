from app.ocr.extractor import extract_text

from app.transformer.invoice_embeddings import (
    InvoiceEmbeddingModel
)

from app.transformer.similarity_detector import (
    InvoiceSimilarityDetector
)


# ==========================================
# READ INVOICE
# ==========================================

invoice_path = "data/invoices/sample.png"

text = extract_text(invoice_path)


print("\n========== INVOICE TEXT ==========\n")

print(text)


# ==========================================
# LOAD TRANSFORMER
# ==========================================

print("\n========== TRANSFORMER ==========\n")

model = InvoiceEmbeddingModel()


# ==========================================
# CREATE EMBEDDINGS
# ==========================================

embedding_1 = model.encode(text)

embedding_2 = model.encode(text)


# ==========================================
# CALCULATE SIMILARITY
# ==========================================

similarity = (
    InvoiceSimilarityDetector
    .cosine_similarity(
        embedding_1,
        embedding_2
    )
)


print("\n========== SIMILARITY ==========\n")

print(
    "Similarity:",
    round(similarity, 4)
)


# ==========================================
# DUPLICATE CHECK
# ==========================================

duplicate = (
    InvoiceSimilarityDetector
    .is_duplicate(
        similarity
    )
)


print(
    "Duplicate:",
    duplicate
)