from flask import Flask, render_template, request
from pathlib import Path
import json

root_dir = Path(__file__).parent.parent

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

dotenv_file = root_dir.joinpath('.env')

if dotenv_file.is_file():
    with open(dotenv_file, "r") as f:
        for line in f.readlines():
            values = line.rstrip().split('=')
            if len(values) == 2:
                dotenv_values[values[0]] = values[1]

DEBUG = bool(int(dotenv_values.get("DEBUG", "1")))
HOST = dotenv_values.get("HOST", "127.0.0.1")
PORT = int(dotenv_values.get("PORT", 7777))

info_json_file = root_dir.joinpath("info.json")

app = Flask(
    "Portfolio Website",
    template_folder=root_dir.joinpath("templates"),
    static_folder=root_dir.joinpath("static")
)

@app.route('/')
def index():
    with open(info_json_file, "r", encoding="utf-8") as f:
        context = json.loads(f.read())
        if context['about_me']['description']:
            for i, line in enumerate(context['about_me']['description']):
                context['about_me']['description'][i] = emojify(line)
    
    return render_template("index.html", **context)

@app.errorhandler(404)
def error404(error):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)