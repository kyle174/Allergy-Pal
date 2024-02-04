import openai
from openai import OpenAI

client = OpenAI(api_key="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")

def get_ingredients(food):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": "list only ingredients for" + food + "in one python parsable string with only ingredients and commas. inlude common allergens, be sure to include all possibilties"}],
        stream=True,
    )

    return stream


result = ""
stream = get_ingredients("pho")
for part in stream:
    result += part.choices[0].delta.content or ""

result = result.split(", ")
result[-1].strip(".")
print(result)
