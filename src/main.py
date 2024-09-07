from flask import Flask, render_template
import json

def emojify(text: str) -> str:
    new_text = text
    
    words = text.split()
    emojis = []
    
    for word in words:
        if word.startswith("emoji:"):
            emojis.append(word.removeprefix("emoji:"))
    
    for emoji in emojis:
        new_text = new_text.replace(f"emoji:{emoji}", f"<img class=\"emoji_icon\" src=\"/static/img/emoji_{emoji}.png\"></img>")
    
    return new_text

dotenv_values = {}

with open(".env", "r") as f:
    for line in f.readlines():
        values = line.rstrip().split('=')
        if len(values) == 2:
            dotenv_values[values[0]] = values[1]
            
DEBUG = bool(int(dotenv_values.get("DEBUG", "0")))
HOST = dotenv_values.get("HOST", "127.0.0.1")
PORT = int(dotenv_values.get("PORT", 7777))

app = Flask("Portfolio Website", template_folder="./templates")

@app.route('/')
def index():
    with open("info.json", "r", encoding="utf-8") as f:
        context = json.loads(f.read())
        if context['about_me']['description']:
            context['about_me']['description'] = emojify(context['about_me']['description'])
    
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)