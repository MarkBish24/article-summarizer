from newspaper import Article
import article_summarizer as summarizer
from bs4 import BeautifulSoup
import requests

def scrape_article(url):

    article = Article(url)
    article.download()
    article.parse()

    text = article.text.strip()
    full_text = text

    if len(text) < 200:
        print("Newpaper missed content, using alternate scraper")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = soup.select(
    "p, div, span"
        )

        manual_text = "\n".join(p.get_text().strip() for p in paragraphs if p.get_text().strip())

        full_text = text + '\n' + manual_text if text else manual_text

    # Defensive defaults
    title = article.title if article.title else "Untitled"
    authors = article.authors if article.authors else []
    summary = summarizer.generate_summary(full_text) if full_text else ""
    publish_date = article.publish_date.isoformat() if article.publish_date else None

    print(summary)
    # Build JSON response
    article_data = {
        "title": title,
        "authors": authors,
        "summary": summary,
        "text": full_text,
        "publish_date": publish_date,
        "url": url
    }

    return article_data