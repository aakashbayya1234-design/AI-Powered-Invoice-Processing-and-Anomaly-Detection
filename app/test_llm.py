from app.llm.invoice_prompt import (
    create_invoice_prompt
)

from app.llm.local_llm import (
    LocalInvoiceLLM
)


invoice_data = {

    "vendor":
        "ABC TECHNOLOGIES PVT LTD",

    "invoice_number":
        "INV-1001",

    "invoice_date":
        "21/08/2026",

    "subtotal":
        115000.0,

    "tax":
        20700.0,

    "total":
        135700.0
}


validation_result = {

    "status":
        "VALID",

    "difference":
        0.0
}


prompt = create_invoice_prompt(

    invoice_data,

    validation_result,

    "NORMAL",

    0.0817,

    1.0
)


print(
    "\n========== LLM ==========\n"
)


llm = LocalInvoiceLLM()


response = llm.generate(
    prompt
)


print(
    "\n========== AI EXPLANATION ==========\n"
)

print(response)