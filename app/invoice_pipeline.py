import pandas as pd
from app.ocr.extractor import extract_text
from app.extraction.items.item_extractor import extract_line_items
from app.validation.invoice_validator import validate_total
from app.extraction.invoice_fields import extract_invoice_data
from app.ml.feature_engineering import create_invoice_features
from app.ml.anomaly_detector import InvoiceAnomalyDetector
from app.llm.invoice_ai import InvoiceAI
from app.agent import InvoiceAgent



# =========================================================
# CONFIGURATION
# =========================================================

IMAGE_PATH = "data/invoices/sample.png"


# =========================================================
# STEP 1 — OCR
# =========================================================

print("\n")
print("=" * 60)
print("STEP 1: OCR")
print("=" * 60)

ocr_text = extract_text(
    IMAGE_PATH
)
print(ocr_text)


# =========================================================
# STEP 2 — FIELD EXTRACTION
# =========================================================

print("\n")
print("=" * 60)
print("STEP 2: FIELD EXTRACTION")
print("=" * 60)

invoice_data = extract_invoice_data(
    ocr_text
)
for key, value in invoice_data.items():

    print(
        f"{key}: {value}"
    )


# =========================================================
# STEP 3 — LINE ITEMS
# =========================================================

print("\n")
print("=" * 60)
print("STEP 3: LINE ITEMS")
print("=" * 60)

line_items = extract_line_items(
    ocr_text
)

for item in line_items:

    print(item)


# =========================================================
# STEP 4 — VALIDATION
# =========================================================

print("\n")
print("=" * 60)
print("STEP 4: VALIDATION")
print("=" * 60)

validation = validate_total(
    invoice_data
)
print(validation)


# =========================================================
# STEP 5 — FEATURES
# =========================================================

print("\n")
print("=" * 60)
print("STEP 5: FEATURES")
print("=" * 60)

features = create_invoice_features(
    invoice_data,
    line_items
)

for key, value in features.items():

    print(
        f"{key}: {value}"
    )


# =========================================================
# STEP 6 — MACHINE LEARNING
# =========================================================

print("\n")
print("=" * 60)
print("STEP 6: ML ANOMALY DETECTION")
print("=" * 60)



detector = InvoiceAnomalyDetector()


# ==========================================
# TRAINING DATA
# ==========================================

training_data = pd.DataFrame({

    "subtotal": [
        10000, 15000, 22000, 18000, 25000,
        30000, 12000, 17000, 21000, 28000,
        500000
    ],

    "tax": [
        1800, 2700, 3960, 3240, 4500,
        5400, 2160, 3060, 3780, 5040,
        90000
    ],

    "total": [
        11800, 17700, 25960, 21240, 29500,
        35400, 14160, 20060, 24780, 33040,
        590000
    ],

    "item_count": [
        3, 4, 5, 3, 6,
        5, 4, 3, 5, 6,
        20
    ],

    "total_quantity": [
        8, 10, 12, 7, 15,
        11, 9, 8, 14, 16,
        200
    ],

    "average_item_price": [
        3333, 3750, 4400, 6000, 4166,
        6000, 3000, 5666, 4200, 4666,
        25000
    ],

    "tax_percentage": [
        18, 18, 18, 18, 18,
        18, 18, 18, 18, 18,
        18
    ]
})


# ==========================================
# TRAIN MODEL
# ==========================================

print(
    "Training invoices:",
    len(training_data)
)


detector.train(
    training_data
)


# ==========================================
# CURRENT INVOICE FEATURES
# ==========================================

X_current = pd.DataFrame(
    [features]
)


# ==========================================
# PREDICT
# ==========================================

anomaly_result = detector.predict(
    X_current
)


result = anomaly_result[0]


anomaly_status = result[
    "status"
]

anomaly_score = result[
    "anomaly_score"
]


print(
    "Status:",
    anomaly_status
)

print(
    "Anomaly Score:",
    anomaly_score
)


# =========================================================
# STEP 7 — GEMINI ANALYSIS
# =========================================================

print("\n")
print("=" * 60)
print("STEP 7: GENERATIVE AI ANALYSIS")
print("=" * 60)

ai = InvoiceAI()

analysis = ai.analyze_invoice(

    invoice_data,

    line_items,

    validation,

    anomaly_status,

    anomaly_score
)

print(analysis)


# =========================================================
# STEP 8 — AGENTIC AI
# =========================================================

print("\n")
print("=" * 60)
print("STEP 8: AGENTIC AI DECISION")
print("=" * 60)

agent = InvoiceAgent()

decision = agent.decide_action(

    invoice_data,

    validation,

    anomaly_status,

    anomaly_score,

    None
)

print(decision)


# =========================================================
# FINAL PROFESSIONAL REPORT
# =========================================================

print("\n")
print("=" * 70)
print("              AI INVOICE PROCESSING REPORT")
print("=" * 70)

print("\n-------------------- INVOICE DETAILS --------------------")

print(
    f"Vendor          : {invoice_data.get('vendor')}"
)

print(
    f"Invoice Number  : {invoice_data.get('invoice_number')}"
)

print(
    f"Invoice Date    : {invoice_data.get('invoice_date')}"
)

print(
    f"Due Date        : {invoice_data.get('due_date')}"
)


print("\n-------------------- FINANCIAL SUMMARY ------------------")

subtotal = invoice_data.get("subtotal", 0)
tax = invoice_data.get("tax", 0)
total = invoice_data.get("total", 0)

tax_percentage = features.get(
    "tax_percentage",
    0
)

print(
    f"Subtotal        : ₹{subtotal:,.2f}"
)

print(
    f"GST             : ₹{tax:,.2f}"
)

print(
    f"GST Rate        : {tax_percentage:.2f}%"
)

print(
    f"Total Amount    : ₹{total:,.2f}"
)


print("\n-------------------- LINE ITEMS --------------------------")

for item in line_items:

    print(
        f"{item['item']:<15}"
        f"| Qty: {item['quantity']:<3}"
        f"| Unit: ₹{item['unit_price']:>10,.2f}"
        f"| Amount: ₹{item['amount']:>12,.2f}"
    )


print("\n-------------------- VALIDATION -------------------------")

print(
    f"Invoice Status  : {validation.get('status')}"
)

print(
    f"Expected Total  : ₹{validation.get('expected_total', 0):,.2f}"
)

print(
    f"Invoice Total   : ₹{validation.get('invoice_total', 0):,.2f}"
)

print(
    f"Difference      : ₹{validation.get('difference', 0):,.2f}"
)


print("\n-------------------- ML ANALYSIS -------------------------")

print(
    f"Risk Status     : {anomaly_status}"
)

print(
    f"Anomaly Score   : {anomaly_score}"
)


print("\n-------------------- AI ANALYSIS ------------------------")

print(analysis)


print("\n-------------------- AGENT DECISION ---------------------")

print(decision)


# =========================================================
# FINAL STATUS
# =========================================================

if (
    validation.get("status") == "VALID"
    and anomaly_status == "NORMAL"
):

    final_status = "SAFE"

elif (
    validation.get("status") == "ANOMALY"
    or anomaly_status == "ANOMALY"
):

    final_status = "REVIEW REQUIRED"

else:

    final_status = "REVIEW"


print("\n")
print("=" * 70)

print(
    f"                 FINAL STATUS: {final_status}"
)

print("=" * 70)

print(
    "\n========== PIPELINE COMPLETE ==========\n"
)