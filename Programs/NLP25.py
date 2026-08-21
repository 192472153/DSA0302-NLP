from openai import OpenAI

client = OpenAI(api_key="sk-..._IEA")

prompt = "Write a short paragraph about Artificial Intelligence."

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("Generated Text:")
print(response.output_text)
