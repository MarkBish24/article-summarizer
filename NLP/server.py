from flask import Flask, request, jsonify
from flask_cors import CORS
import article_summarizer as summarizer

app = Flask(__name__)
CORS(app)

@app.route("/summarize", methods=["GET", "POST"])
def summarize_route():
    data = request.get_json(silent=True)

    if data and "text" in data:
        text = data["text"]
    else:
        with open("text.txt", "r", encoding="utf-8") as f:
            text = f.read()

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = summarizer.generate_summary(text)

    return jsonify({"summary": summary})

@app.route("/article", methods=["GET", "POST"])
def article_info_route():
    data = request.get_json()
    return jsonify({"message": f"Article received: {data}"})

if __name__ == "__main__":
    app.run(port=4000)