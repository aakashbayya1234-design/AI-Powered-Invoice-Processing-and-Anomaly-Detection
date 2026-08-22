import os
from pathlib import Path

from dotenv import dotenv_values
from google import genai


# ==========================================
# FIND PROJECT ROOT
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ENV_FILE = PROJECT_ROOT / ".env"


# ==========================================
# READ .ENV DIRECTLY
# ==========================================

config = dotenv_values(
    ENV_FILE
)


api_key = config.get(
    "GEMINI_API_KEY"
)


# ==========================================
# CHECK KEY
# ==========================================

if not api_key:

    print("\n========== ERROR ==========\n")

    print(
        "GEMINI_API_KEY was not found."
    )

    print(
        "Environment file:"
    )

    print(
        ENV_FILE
    )

    print(
        "\nKeys detected in .env:"
    )

    print(
        list(config.keys())
    )

    raise SystemExit(1)


print(
    "\n========== GEMINI CONFIGURATION ==========\n"
)

print(
    "Environment file:",
    ENV_FILE
)

print(
    "API key detected: YES"
)


# ==========================================
# CREATE GEMINI CLIENT
# ==========================================

client = genai.Client(
    api_key=api_key
)


# ==========================================
# TEST GEMINI
# ==========================================

print(
    "\n========== GEMINI TEST ==========\n"
)


response = client.models.generate_content(

    model="gemini-3.6-flash",

    contents=(
        "Explain what an invoice is "
        "in one simple sentence."
    )
)


# ==========================================
# DISPLAY RESPONSE
# ==========================================

print(
    "\n========== GEMINI RESPONSE ==========\n"
)

print(
    response.text
)