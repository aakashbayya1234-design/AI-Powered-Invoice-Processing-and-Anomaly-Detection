from sentence_transformers import SentenceTransformer


class InvoiceEmbeddingModel:

    def __init__(self):

        print(
            "Loading local Transformer model..."
        )

        self.model = SentenceTransformer(
            "models/all-MiniLM-L6-v2"
        )

    def encode(self, text):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding