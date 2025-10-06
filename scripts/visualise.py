import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords
import nltk
nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

# -----------------------
# Preprocess text for topics
# -----------------------
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    return words

# -----------------------
# Visualisation
# -----------------------
def visualise(input_file="news_summary.csv", top_n=10):
    df = pd.read_csv(input_file)

    # ---------------------
    # 1. Top topics bar chart
    # ---------------------
    all_words = []
    for summary in df["summary"].dropna():
        all_words.extend(preprocess_text(summary))
    word_freq = Counter(all_words)
    top_words = dict(word_freq.most_common(top_n))

    colors = plt.cm.viridis(range(len(top_words)))
    plt.figure(figsize=(10,5))
    plt.bar(top_words.keys(), top_words.values(), color=colors)
    plt.title(f"Top {top_n} Topics in News Summaries", fontsize=16)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

    # ---------------------
    # 2. Word cloud
    # ---------------------
    text = " ".join(str(s) for s in df["summary"].dropna())
    wc = WordCloud(width=800, height=400, background_color="#f0f0f0",
                   colormap="viridis", stopwords=STOPWORDS, max_words=200).generate(text)
    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Topics", fontsize=16)
    plt.show()

    # ---------------------
    # 3. Sentiment pie chart
    # ---------------------
    if "sentiment" in df.columns:
        sentiment_counts = df["sentiment"].value_counts()
        colors = ["#2ca02c", "#ff7f0e", "#d62728"]  # green, orange, red
        plt.figure(figsize=(6,6))
        plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%",
                colors=colors, startangle=140, wedgeprops={"edgecolor": "white"})
        plt.title("Sentiment Distribution in Summaries", fontsize=16)
        plt.show()

    print("Visualisation complete!")

# -----------------------
# Execute
# -----------------------
if __name__ == "__main__":
    visualise("news_summary.csv", top_n=10)
