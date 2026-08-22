import numpy as np

from sklearn.ensemble import IsolationForest


class InvoiceAnomalyDetector:

    def __init__(self):

        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.10,
            random_state=42
        )

        self.is_trained = False


    def train(self, X):

        self.model.fit(X)

        self.is_trained = True


    def predict(self, X):

        if not self.is_trained:
            raise ValueError(
                "Model has not been trained yet."
            )

        predictions = self.model.predict(X)

        scores = self.model.decision_function(X)

        results = []

        for prediction, score in zip(
            predictions,
            scores
        ):

            if prediction == 1:
                status = "NORMAL"
            else:
                status = "ANOMALY"

            results.append({
                "status": status,
                "anomaly_score": round(
                    float(score),
                    4
                )
            })

        return results