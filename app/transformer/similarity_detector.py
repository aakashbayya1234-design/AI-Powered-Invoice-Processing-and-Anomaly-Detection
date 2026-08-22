import numpy as np


class InvoiceSimilarityDetector:

    @staticmethod
    def cosine_similarity(
        embedding_a,
        embedding_b
    ):

        embedding_a = np.asarray(
            embedding_a,
            dtype=float
        )

        embedding_b = np.asarray(
            embedding_b,
            dtype=float
        )

        numerator = np.dot(
            embedding_a,
            embedding_b
        )

        denominator = (
            np.linalg.norm(embedding_a)
            *
            np.linalg.norm(embedding_b)
        )

        if denominator == 0:
            return 0.0

        return float(
            numerator / denominator
        )

    @staticmethod
    def is_duplicate(
        similarity,
        threshold=0.90
    ):

        return similarity >= threshold