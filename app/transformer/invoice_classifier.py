from transformers import pipeline


class InvoiceTextClassifier:

    def __init__(self):

        print("Loading Transformer model...")

        self.classifier = pipeline(
            "fill-mask",
            model="distilbert/distilbert-base-uncased"
        )

    def classify(self, text):

        text = text[:1000]

        prompt = text + " This document is a [MASK]."

        result = self.classifier(prompt)

        return result