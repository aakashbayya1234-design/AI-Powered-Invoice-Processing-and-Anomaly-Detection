import pandas as pd

from app.ml.invoice_dataset import (
    create_training_dataset
)

from app.ml.anomaly_detector import (
    InvoiceAnomalyDetector
)


# ==========================================
# CREATE TRAINING DATA
# ==========================================

df = create_training_dataset(
    number_of_invoices=500
)


print(
    "\n========== TRAINING DATA ==========\n"
)

print(df.head())

print(
    f"\nTotal training invoices: {len(df)}"
)


# ==========================================
# FEATURES
# ==========================================

features = [

    "subtotal",

    "tax",

    "total",

    "item_count",

    "total_quantity",

    "average_item_price",

    "tax_percentage"
]


X = df[features]


# ==========================================
# TRAIN MODEL
# ==========================================

detector = InvoiceAnomalyDetector()

detector.train(X)


print(
    "\n========== MODEL TRAINED ==========\n"
)


# ==========================================
# TEST INVOICES
# ==========================================

test_invoices = pd.DataFrame(

    [

        [
            20000,
            3600,
            23600,
            4,
            10,
            5000,
            18
        ],

        [
            25000,
            4500,
            29500,
            5,
            12,
            5000,
            18
        ],

        [
            900000,
            162000,
            1062000,
            50,
            500,
            18000,
            18
        ]

    ],

    columns=features
)


# ==========================================
# PREDICTION
# ==========================================

results = detector.predict(
    test_invoices
)


print(
    "\n========== PREDICTIONS ==========\n"
)


for i, result in enumerate(
    results,
    start=1
):

    print(
        f"Invoice {i}: "
        f"{result['status']} | "
        f"Score: "
        f"{result['anomaly_score']}"
    )