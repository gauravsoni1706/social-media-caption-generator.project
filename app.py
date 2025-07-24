from flask import Flask, render_template, request, jsonify
from captions import generate_caption

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    keywords = data.get("keywords")
    platform = data.get("platform")
    tone = data.get("tone")
    caption_data = generate_caption(keywords, platform, tone)
    return jsonify(caption_data)

if __name__ == "__main__":
    app.run(debug=True)