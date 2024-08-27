from transformers import MT5ForConditionalGeneration, MT5Tokenizer

model_name = "google/mt5-small"
tokenizer = MT5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

def translate_text(request):
    inputs = tokenizer(request.text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"])
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text
