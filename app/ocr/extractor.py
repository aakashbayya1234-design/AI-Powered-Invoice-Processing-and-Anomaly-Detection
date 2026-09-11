import cv2
import pytesseract
from app.ocr.extractor import extract_text

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    processed = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return processed


def extract_text(image_path):

    processed_image = preprocess_image(
        image_path
    )

    text = pytesseract.image_to_string(
        processed_image
    )

    return text


if __name__ == "__main__":

    invoice_path = "data/invoices/sample.png"

    print("Processing invoice...")

    text = extract_text(invoice_path)

    print("\n========== OCR RESULT ==========\n")

    print(text)

    print("\n========== END ==========\n")
