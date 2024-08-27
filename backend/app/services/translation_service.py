import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure you have set your OpenAI API key as an environment variable
# export OPENAI_API_KEY='your-api-key'


def translate_text(request):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a culturally aware translation assistant specializing in nuanced dialects.",
                },
                {
                    "role": "user",
                    "content": f"""Translate the following text from {request.source_lang} to {request.target_lang}, considering the language style, social norms, and colloquialisms.
                    
                                    Pay close attention to cultural context and ensure that idiomatic expressions are accurately conveyed in the target language.

                                    Additional Instructions:

                                    Maintain Context: Consider the historical context of the text, including the year, to ensure that the translation accurately reflects the intended meaning.

                                    Maintain Authenticity: Ensure the translation retains the original tone, sentiment, and meaning. Pay attention to subtle nuances, including formality, humor, and connotation in the source text.

                                    Cultural Sensitivity: Use culturally appropriate phrases and avoid expressions that may be considered offensive or insensitive in the target language. Take into account the cultural context of the specified era.

                                    Formatting: Present the translation in a way that reflects the format and structure of the original text. Maintain paragraphs, punctuation, and any stylistic elements.

                                    Translation Integrity: If any part of the text contains content that does not translate directly or loses meaning in the target language, provide a brief explanation or alternative translation.

                                    Regional Variation: {request.regional_variation} {request.target_lang}
                                    Generational Influence: {request.generational_influence}
                                    Socio-Economic Context: {request.socio_economic_context}
                                    Cultural Influences: {', '.join(request.cultural_influences)}
                                    Code-Switching: {'Enabled' if request.code_switching else 'Disabled'}
                                    Geographical Setting: {request.geographical_setting}

                                    Output: Only return the translated text without additional information or explanations unless clarification is requested by the user.


                               Here is the text to translate:
                               {request.text}""",
                },
            ],
            max_tokens=1000,
        )
        translated_text = response.choices[0].message.content.strip()
        return translated_text
    except Exception as e:
        return f"An error occurred: {str(e)}"
