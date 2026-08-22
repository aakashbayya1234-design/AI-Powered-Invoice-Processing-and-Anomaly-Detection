from app.agent import InvoiceAgent


invoice_data = {

    "vendor":
        "ABC TECHNOLOGIES PVT LTD",

    "invoice_number":
        "INV-1001",

    "total":
        135700.0
}


validation = {

    "status":
        "VALID",

    "difference":
        0.0
}


anomaly_status = "NORMAL"

anomaly_score = 0.0817

similarity_score = 0.12


print(
    "\n========== AGENTIC AI ==========\n"
)


agent = InvoiceAgent()


decision = agent.decide_action(

    invoice_data,

    validation,

    anomaly_status,

    anomaly_score,

    similarity_score
)


print(
    "\n========== AGENT DECISION ==========\n"
)

print(decision)