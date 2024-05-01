import openai

def fetch_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

print(fetch_response("Hello, world! This is a test prompt."))
