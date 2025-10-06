import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)   # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)               # keep only letters
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if w not in STOPWORDS and len(w) > 2]
    return " ".join(tokens)

def preprocess_file(input_file="news_raw.csv", output_file="news_clean.csv"):
    df = pd.read_csv(input_file)
    df["clean_content"] = df["content"].apply(clean_text)
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_file()
