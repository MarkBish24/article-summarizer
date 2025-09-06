import spacy
from collections import Counter
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    """
    Generates a summary of the input text.
    Dynamically adjusts min_length and max_length based on the number of sentences.
    """
    doc = nlp(text)

    # Count words ignoring stop words and non-alpha tokens
    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    word_freq = Counter(words)
    max_freq = max(word_freq.values(), default=1)
    for word in word_freq:
        word_freq[word] /= max_freq  # normalize frequencies

    # Score sentences
    sentence_scores = {}
    sentences = list(doc.sents)
    num_sentences_to_select = max(3, round(len(sentences) / 4))  # top quarter of sentences
    for sent in sentences:
        for token in sent:
            if token.text.lower() in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[token.text.lower()]

    # Select top sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences_to_select]
    selected_text = " ".join([sent.text for sent in top_sentences])

    # Dynamically set min/max lengths (approx. 30 tokens per sentence)
    min_length = max(25, 30 * min(len(top_sentences), 5))
    max_length = 30 * len(top_sentences) + 20  # slightly longer than number of sentences

    # Generate final summary
    summary = summarizer_pipeline(selected_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']