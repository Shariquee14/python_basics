from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LG6OlkwsqYpIYv9owsxY4Mp3yy5naSbUfvaU2aZqlJqA"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Why Human more intelligent than AI? Explain this in few words."
)
print(interaction.output_text)