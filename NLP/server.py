from flask import Flask, request, jsonify
from flask_cors import CORS
import article_summarizer as summarizer
import article_scraper as scraper

app = Flask(__name__)
CORS(app)

#Test Article https://www.aljazeera.com/news/liveblog/2025/9/5/live-israel-kills-18-overnight-as-intense-strikes-flatten-gaza-city

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

@app.route("/article", methods=["POST"])
def article_info_route():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = data["url"]

    try:
        article_json = scraper.scrape_article(url)
        return jsonify(article_json)
    except Exception as e:
        print("Error scraping article:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=4000, debug=True)