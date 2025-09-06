import { useState } from "react";
import URLTab from "./components/URLTab.jsx";
import ArticleDisplay from "./components/ArticleDisplay.jsx";

function App() {
  const [cachedArticles, setCachedArticles] = useState([]);
  const [articleData, setArticleData] = useState({});
  const [isSubmittingUrL, setIsSubmittingUrl] = useState(true);

  return (
    <>
      {isSubmittingUrL ? (
        <URLTab
          setArticleData={setArticleData}
          setIsSubmittingUrl={setIsSubmittingUrl}
        />
      ) : (
        <ArticleDisplay
          articleData={articleData}
          setIsSubmittingUrl={setIsSubmittingUrl}
        />
      )}
    </>
  );
}

export default App;
