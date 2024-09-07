from flask import Flask, render_template
import json

HOST = '127.0.0.1'
PORT = 7777
DEBUG = True

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