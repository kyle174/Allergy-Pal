import openai
from openai import OpenAI

client = OpenAI(api_key="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")

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "list ingredients for pho that are common allergens in one string"}],
    stream=True,
)

result = ""
for part in stream:
    result += part.choices[0].delta.content or ""

result = result.split(", ")
result[-1].strip(".")
print(result)