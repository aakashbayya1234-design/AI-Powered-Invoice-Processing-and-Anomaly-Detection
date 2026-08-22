import os
from pathlib import Path

from dotenv import dotenv_values
from google import genai


class InvoiceAI:

    def __init__(self):

        # Find project root
        project_root = Path(__file__).resolve().parent.parent.parent

        # Load .env
        env_file = project_root / ".env"

        config = dotenv_values(env_file)

        api_key = config.get("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found."
            )

        # Create Gemini client
        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-3.6-flash"

    def analyze_invoice(
        self,
        invoice_data,
        line_items,
        validation,
        anomaly_status,
        anomaly_score
    ):

        prompt = f"""
You are an expert AI financial invoice analyst.

Analyze the following invoice.

========== INVOICE DATA ==========

Vendor:
{invoice_data.get("vendor")}

Invoice Number:
{invoice_data.get("invoice_number")}

Invoice Date:
{invoice_data.get("invoice_date")}

Due Date:
{invoice_data.get("due_date")}

Subtotal:
₹{invoice_data.get("subtotal")}

Tax:
₹{invoice_data.get("tax")}

Total:
₹{invoice_data.get("total")}


========== LINE ITEMS ==========

{line_items}


========== VALIDATION ==========

{validation}


========== MACHINE LEARNING ANOMALY DETECTION ==========

Status:
{anomaly_status}

Anomaly Score:
{anomaly_score}


========== TASK ==========

Provide a professional invoice analysis.

Include:

1. Invoice summary
2. Vendor information
3. Financial summary
4. Tax analysis
5. Validation result
6. Anomaly risk
7. Possible reasons for anomaly
8. Business recommendation

Do not invent information that is not present.
Clearly distinguish between confirmed facts and possible risks.

Keep the response concise and professional.
"""

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt
        )

        return response.text