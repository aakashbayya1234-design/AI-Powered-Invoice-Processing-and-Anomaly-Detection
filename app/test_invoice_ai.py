from app.llm.invoice_ai import InvoiceAI


invoice_data = {

    "vendor":
        "ABC TECHNOLOGIES PVT LTD",

    "invoice_number":
        "INV-1001",

    "invoice_date":
        "21/08/2026",

    "due_date":
        "05/09/2026",

    "subtotal":
        115000.0,

    "tax":
        20700.0,

    "total":
        135700.0
}


line_items = [

    {
        "item": "Laptop",
        "quantity": 2,
        "unit_price": 50000.0,
        "amount": 100000.0
    },

    {
        "item": "Keyboard",
        "quantity": 5,
        "unit_price": 2000.0,
        "amount": 10000.0
    },

    {
        "item": "Mouse",
        "quantity": 5,
        "unit_price": 1000.0,
        "amount": 5000.0
    }
]


validation = {

    "status":
        "VALID",

    "expected_total":
        135700.0,

    "invoice_total":
        135700.0,

    "difference":
        0.0
}


anomaly_status = "NORMAL"

anomaly_score = 0.0817


print(
    "\n========== GENERATING AI ANALYSIS ==========\n"
)


ai = InvoiceAI()


analysis = ai.analyze_invoice(

    invoice_data,

    line_items,

    validation,

    anomaly_status,

    anomaly_score
)


print(
    "\n========== AI INVOICE ANALYSIS ==========\n"
)

print(analysis)