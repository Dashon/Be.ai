import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure you have set your OpenAI API key as an environment variable
# export OPENAI_API_KEY='your-api-key'


def translate_text(request):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that translates text."},
        {"role": "user", "content": f"Translate the following text from {request.source_lang} to {request.target_lang}: {request.text}"}
    ],
    max_tokens=1000)
    translated_text = response.choices[0].message.content.strip()
    return translated_text
