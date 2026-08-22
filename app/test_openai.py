from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI()


response = client.responses.create(
    model="gpt-5.5",
    input="Explain in one sentence what an invoice is."
)


print("\n========== OPENAI TEST ==========\n")

print(response.output_text)