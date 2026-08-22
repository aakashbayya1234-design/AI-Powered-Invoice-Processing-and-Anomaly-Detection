from app.ocr.extractor import extract_text

from app.extraction.items.item_extractor import (
    extract_line_items
)


invoice_path = "data/invoices/sample.png"


print("Reading invoice...")

text = extract_text(invoice_path)


items = extract_line_items(text)


print("\n========== LINE ITEMS ==========\n")


for item in items:

    print(
        f"Item: {item['item']}"
    )

    print(
        f"Quantity: {item['quantity']}"
    )

    print(
        f"Unit Price: ₹{item['unit_price']}"
    )

    print(
        f"Amount: ₹{item['amount']}"
    )

    print("------------------------------")