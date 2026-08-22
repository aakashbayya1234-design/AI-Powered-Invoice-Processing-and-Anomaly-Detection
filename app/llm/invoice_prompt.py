def create_invoice_prompt(
    invoice_data,
    validation_result,
    anomaly_status,
    anomaly_score,
    similarity=None
):

    prompt = f"""
You are an AI financial invoice analyst.

Analyze the following invoice.

Vendor:
{invoice_data.get("vendor")}

Invoice Number:
{invoice_data.get("invoice_number")}

Invoice Date:
{invoice_data.get("invoice_date")}

Subtotal:
₹{invoice_data.get("subtotal")}

Tax:
₹{invoice_data.get("tax")}

Total:
₹{invoice_data.get("total")}

Validation Status:
{validation_result.get("status")}

Validation Difference:
₹{validation_result.get("difference")}

ML Anomaly Status:
{anomaly_status}

ML Anomaly Score:
{anomaly_score}
"""

    if similarity is not None:

        prompt += f"""

Semantic Similarity:
{similarity}
"""

    prompt += """

Provide a concise financial risk analysis.

Explain:

1. Whether the invoice appears valid.
2. Whether there are unusual values.
3. Whether the invoice should be reviewed.
4. The main reasons for your decision.

Do not invent information that is not present in the invoice.
"""

    return prompt