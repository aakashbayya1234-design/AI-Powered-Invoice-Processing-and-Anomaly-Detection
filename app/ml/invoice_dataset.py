import random
import pandas as pd


def create_training_dataset(number_of_invoices=500):

    random.seed(42)

    data = []

    for _ in range(number_of_invoices):

        item_count = random.randint(2, 8)

        total_quantity = random.randint(
            item_count,
            item_count * 5
        )

        average_item_price = random.uniform(
            500,
            15000
        )

        subtotal = round(
            total_quantity * average_item_price,
            2
        )

        tax_percentage = random.choice(
            [5, 12, 18]
        )

        tax = round(
            subtotal * tax_percentage / 100,
            2
        )

        total = round(
            subtotal + tax,
            2
        )

        data.append({
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
            "item_count": item_count,
            "total_quantity": total_quantity,
            "average_item_price": round(
                average_item_price,
                2
            ),
            "tax_percentage": tax_percentage
        })

    return pd.DataFrame(data)