import { useState } from "react";
import "./ArticleDisplay.css";
import { IoMdArrowDropdown } from "react-icons/io";

export default function ArticleDisplay({ articleData, setIsSubmittingUrl }) {
  const images = articleData.images || [];
  const [current, setCurrent] = useState(0);

  const prevSlide = () =>
    setCurrent((current - 1 + images.length) % images.length);
  const nextSlide = () => setCurrent((current + 1) % images.length);

  return (
    <div className="article-container">
      <h1 className="article-title">{articleData.title}</h1>
      <h2 className="article-authors">
        {articleData.authors?.length > 0
          ? articleData.authors.join(", ")
          : "Unknown author"}
      </h2>
      <p className="article-summary">{articleData.summary}</p>

      {images.length > 0 && (
        <div className="carousel-img-display" style={{ position: "relative" }}>
          {/* Image */}
          <img
            className="article-img"
            src={images[current]}
            alt={`Slide ${current + 1}`}
          />

          {/* Buttons */}
          <button className="carousel-btn left" onClick={prevSlide}>
            <IoMdArrowDropdown style={{ transform: "rotate(90deg)" }} />
          </button>
          <button className="carousel-btn right" onClick={nextSlide}>
            <IoMdArrowDropdown style={{ transform: "rotate(-90deg)" }} />
          </button>

          {/* HUD */}
          <div className="carousel-hud">
            {images.map((_, idx) => (
              <span
                key={idx}
                onClick={() => setCurrent(idx)}
                className={idx === current ? "dot active" : "dot"}
              ></span>
            ))}
          </div>
        </div>
      )}
      <button
        className="return-btn"
        onClick={() => {
          setIsSubmittingUrl(true);
        }}
      >
        Summarize another article
      </button>
    </div>
  );
}
