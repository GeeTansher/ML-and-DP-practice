import openai
openai.api_key = "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"

def generate_text(prompt):
    model_engine = "davinci"  # or any other model you prefer
    stop=["\n", "!", ".", "?"]
    prompt = prompt.strip()
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message


prompt = "can i pet a cat?"
response = generate_text(prompt)
print(response)
