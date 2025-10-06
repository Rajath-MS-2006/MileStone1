import os
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_live_news(queries, page_size=100):
    articles = []
    from_date = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y-%m-%d")
    to_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for q in queries:
        params = {
            "q": q,
            "language": "en",
            "from": from_date,
            "to": to_date,
            "sortBy": "publishedAt",
            "pageSize": page_size,
            "apiKey": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for article in data.get("articles", []):
                articles.append({
                    "query": q,
                    "source": article["source"]["name"],
                    "title": article["title"],
                    "url": article["url"],
                    "published_at": article["publishedAt"],
                    "content": article.get("content"),
                    "fetched_at": datetime.now(timezone.utc).isoformat()
                })
        else:
            print(f"Error fetching {q}: {response.status_code}")
    return pd.DataFrame(articles)

if __name__ == "__main__":
    df = fetch_live_news(["artificial intelligence", "machine learning", "competitor_name"])
    df.to_csv("news_raw.csv", index=False)
    print(f"Fetched {len(df)} articles for the past month")
