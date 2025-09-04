# To find the most common sentences
import spacy
from collections import Counter
# To generate a new summary with the organized sentences
import torch
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# Get Most Useful sentences
def get_most_useful_sentences(text):
    #Process the text throught the spacy npl
    doc = nlp(text)

    #get each token in the doc where it a word and isn't a common word like "the", "a", or "is"
    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    #Create a counter for each of the words to find the most common
    word_freq = Counter(words)

    #Sort by most common words
    max_freq = max(word_freq.values(), default=1)
    #normalize it to give it a score of most frequent words scale count to 0-1(Adds a weight)
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq

    #Score sentence dictionary,( Basic Hashmap frequency algorithm)
    sentence_scores = {}
    num_sentences = max(3, int(round(len(list(doc.sents)) / 4)))
    sentences = [sent for sent in doc.sents]
    print("Number of sentences:", len(sentences))
    # go through each sentence of each word in the doc again 
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq: # if the word is in the freq list add it's weight
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word.text.lower()]

    #get the top sentences with the highest score
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    summary = " ".join([sent.text for sent in summary_sentences])

    return summary  

def generate_summary(text):
    summary = summarizer_pipeline(get_most_useful_sentences(text), max_length=120, min_length=50, do_sample=False)

    return summary[0]['summary_text']