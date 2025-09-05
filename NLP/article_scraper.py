from newspaper import Article

def scrape_article(url):

    article = Article(url)

    article.download()
    article.parse()

    # Build JSON response
    article_data = {
        "title": article.title,
        "authors": article.authors,
        "text": article.text,
        "publish_date": article.publish_date.isoformat() if article.publish_date else None,
        "url": url
    }

    return article_data