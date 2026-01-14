🧠 AI-Powered Strategic Intelligence Platform (News Monitoring)
📌 Project Overview

This project is part of Infosys Springboard Internship – Milestone 1.
It focuses on building a real-time, AI-powered strategic intelligence system that collects, preprocesses, summarises, and visualises 1-month news data related to target topics such as Artificial Intelligence, Machine Learning, or competitors.

The goal is to automatically:

Fetch live news articles from trusted sources

Clean and preprocess unstructured text

Generate summaries and sentiment analysis

Visualise market trends and topic insights

⚙️ Tech Stack

Python 3.12+

APIs: NewsAPI

Libraries: pandas, nltk, textblob, matplotlib, wordcloud, requests, dotenv

## 🧩 Project Pipeline
```text
┌────────────────────────┐
│ 1️⃣ live_news_fetch.py  │ → Fetch last 1-month news via API
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ 2️⃣ pre_process.py      │ → Clean and normalize text data
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ 3️⃣ summarise.py        │ → Summarise and assign sentiment
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ 4️⃣ visualise.py        │ → Generate topic graphs & word cloud
└────────────────────────┘
```

📁 File Descriptions
📰 live_news_fetch.py

Fetches 1-month news articles using NewsAPI.

Saves data to news_raw.csv.

Fields include title, source, content, published date, etc.

🧼 pre_process.py

Cleans text by:

Removing URLs, special symbols, and stopwords.

Lowercasing and tokenizing words.

Saves cleaned dataset as news_clean.csv.

✂️ summarise.py

Uses frequency-based extractive summarization to condense articles.

Performs sentiment analysis using TextBlob:

Positive, Negative, Neutral classification.

Saves summarized data to news_summary.csv.

📊 visualise.py

Generates three key visuals:

Bar chart → Top trending topics.

Word cloud → Frequent keywords in news.

Pie chart → Sentiment distribution.

Helps identify key market trends and overall tone.

1️⃣Install Dependencies
pip install -r requirements.txt

2️⃣ Set Up Environment Variable

Create a .env file in your root folder and add:

NEWS_API_KEY=your_newsapi_key_here


Get your free key from https://newsapi.org/register
.
🚀 Execution Steps

Fetch news:

python live_news_fetch.py


Preprocess text:

python pre_process.py


Summarise and analyze sentiment:

python summarise.py


Generate visuals:

python visualise.py

📊 Output Files
File Name	Description
news_raw.csv	Raw fetched articles
news_clean.csv	Cleaned text data
news_summary.csv	Summaries + sentiment
Visual Outputs	Charts & word clouds displayed via Matplotlib
🌟 Insights You Get

✅ Trending topics in your industry
✅ Most active news sources
✅ Positive / Negative media sentiment trends
✅ Keyword clusters (WordCloud)
🧩 Requirements Summary

All dependencies are listed in requirements.txt:

pandas → data handling

requests → API calls

python-dotenv → manage API keys

nltk → text tokenization and stopwords

textblob → sentiment analysis

matplotlib → charts

wordcloud → topic visualization
