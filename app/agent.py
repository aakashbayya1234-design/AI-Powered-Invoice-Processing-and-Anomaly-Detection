import os
from pathlib import Path

from dotenv import dotenv_values
from google import genai


class InvoiceAgent:

    def __init__(self):

        # Find project root
        project_root = (
            Path(__file__).resolve().parent.parent
        )

        # Load .env
        env_file = project_root / ".env"

        config = dotenv_values(env_file)

        api_key = config.get(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GEMINI_API_KEY not found."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-3.6-flash"


    def decide_action(

        self,
        invoice_data,
        validation,
        anomaly_status,
        anomaly_score,
        similarity_score=None

    ):

        prompt = f"""
You are an intelligent invoice-processing agent.

Your job is to decide what action should be
taken for an invoice.

========== INVOICE ==========

Vendor:
{invoice_data.get("vendor")}

Invoice Number:
{invoice_data.get("invoice_number")}

Total:
₹{invoice_data.get("total")}


========== VALIDATION ==========

Status:
{validation.get("status")}

Difference:
{validation.get("difference")}


========== ANOMALY DETECTION ==========

Status:
{anomaly_status}

Anomaly Score:
{anomaly_score}


========== DUPLICATE DETECTION ==========

Similarity Score:
{similarity_score}


========== POSSIBLE ACTIONS ==========

APPROVE
REVIEW
REJECT
BLOCK_DUPLICATE


========== DECISION RULES ==========

If invoice validation is INVALID:
choose REJECT.

If anomaly detection indicates ANOMALY:
choose REVIEW.

If similarity score is very high:
choose BLOCK_DUPLICATE.

If the invoice is valid, normal and not duplicate:
choose APPROVE.


Return your response in exactly this format:

ACTION: <APPROVE/REVIEW/REJECT/BLOCK_DUPLICATE>

REASON: <short explanation>

RISK_LEVEL: <LOW/MEDIUM/HIGH>

CONFIDENCE: <0-100>
"""

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt
        )

        return response.text