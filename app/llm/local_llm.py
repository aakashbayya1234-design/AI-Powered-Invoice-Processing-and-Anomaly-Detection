from transformers import pipeline


class LocalInvoiceLLM:

    def __init__(self):

        print(
            "Loading local LLM..."
        )

        self.generator = pipeline(
            "text-generation",
            model="gpt2"
        )

    def generate(self, prompt):

        result = self.generator(
            prompt,
            max_new_tokens=150,
            do_sample=False,
            pad_token_id=50256
        )

        generated_text = result[0]["generated_text"]

        return generated_text