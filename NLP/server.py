from flask import Flask, request, jsonify
import article_summarizer as summarizer

app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize_route():
    
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = summarizer.generate_summary(text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(port=4000)