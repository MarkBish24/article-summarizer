import { useState } from "react";
import URLTab from "./components/URLTab.jsx";

function App() {
  const [articles, setArticles] = useState([]);
  const [isSubmittingURL, setIsSubmittingUrl] = useState(true);

  return <>{isSubmittingURL ? <URLTab /> : null}</>;
}

export default App;
