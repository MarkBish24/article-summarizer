import { useState } from "react";

// *** How the article data is organized
// article_data = {
//     "title": article.title,
//     "authors": article.authors,
//     "text": article.text,
//     "publish_date": article.publish_date.isoformat() if article.publish_date else None,
//     "url": url
// }

export default function ArticleDisplay({ articleData }) {
  return (
    <div>
      <h1>{articleData.title}</h1>
      <h2>{articleData.authors}</h2>
      <p>{articleData.summary}</p>
    </div>
  );
}
