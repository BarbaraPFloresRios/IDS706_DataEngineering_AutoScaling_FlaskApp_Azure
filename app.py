from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

model_name = 'Helsinki-NLP/opus-mt-en-es'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html', input_text="", translated_text="")

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return render_template('index.html', input_text=input_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
