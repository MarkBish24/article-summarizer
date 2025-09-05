import { useState } from "react";
import "./URLTab.css";

export default function URLTab() {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitting URL:", url);
  };

  return (
    <form onSubmit={handleSubmit} className="url-form">
      <input
        type="text"
        placeholder="Enter article URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="url-input"
      />
      <button className="url-submit-btn" type="submit">
        Submit
      </button>
    </form>
  );
}
