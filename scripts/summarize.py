import pandas as pd
import re
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
from textblob import TextBlob

# Download required NLTK data
nltk.download("punkt")
nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

# -----------------------
# Text cleaning
# -----------------------
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # keep letters only
    return text

# -----------------------
# Summarisation
# -----------------------
def summarise_text(text, n=2):
    if not isinstance(text, str) or len(text.split()) < 30:
        return text

    sentences = sent_tokenize(text)
    words = word_tokenize(clean_text(text))
    freq = Counter(w for w in words if w not in STOPWORDS)

    sentence_scores = {}
    for sent in sentences:
        sentence_scores[sent] = sum(freq.get(w,0) for w in word_tokenize(clean_text(sent)))

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    return " ".join(top_sentences)

# -----------------------
# Sentiment analysis
# -----------------------
def analyze_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        return "positive"
    elif polarity < -0.05:
        return "negative"
    else:
        return "neutral"

# -----------------------
# Main summarisation function
# -----------------------
def summarise_file(input_file="news_clean.csv", output_file="news_summary.csv", sentences_per_article=2):
    df = pd.read_csv(input_file)
    df["summary"] = df["clean_content"].apply(lambda x: summarise_text(x, n=sentences_per_article))
    df["sentiment"] = df["summary"].apply(analyze_sentiment)
    df.to_csv(output_file, index=False)
    print(f"Summarisation + sentiment done! Saved to {output_file}")
    return df

# -----------------------
# Execute
# -----------------------
if __name__ == "__main__":
    summarise_file("news_clean.csv", "news_summary.csv", sentences_per_article=2)
