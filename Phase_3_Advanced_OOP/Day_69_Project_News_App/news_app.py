# ============================================================
# Day 69: Project — Automatic News App using a News API
# ============================================================
# Uses NewsAPI.org (free tier)
# Get your API key at: https://newsapi.org/
# pip install requests
# ============================================================

import requests
import json
from datetime import datetime

API_KEY  = "YOUR_API_KEY_HERE"   # ← Replace with your key from newsapi.org
BASE_URL = "https://newsapi.org/v2"

def get_top_headlines(category="technology", country="in", count=5):
    """Fetch top headlines from NewsAPI."""
    url = f"{BASE_URL}/top-headlines"
    params = {
        "apiKey"  : API_KEY,
        "category": category,
        "country" : country,
        "pageSize": count,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_news_by_keyword(keyword, count=5):
    """Fetch news articles by keyword."""
    url = f"{BASE_URL}/everything"
    params = {
        "apiKey"  : API_KEY,
        "q"       : keyword,
        "pageSize": count,
        "sortBy"  : "publishedAt",
        "language": "en",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def display_articles(data):
    """Display articles in a readable format."""
    articles = data.get("articles", [])
    if not articles:
        print("No articles found.")
        return

    print(f"\n{'='*60}")
    print(f"  Found {len(articles)} articles (total: {data.get('totalResults', '?')})")
    print("=" * 60)

    for i, article in enumerate(articles, 1):
        title       = article.get("title", "No title")
        source      = article.get("source", {}).get("name", "Unknown")
        published   = article.get("publishedAt", "")[:10]
        url         = article.get("url", "")
        description = article.get("description") or "No description available."

        print(f"\n{i}. [{source}] {published}")
        print(f"   📰 {title}")
        print(f"   {description[:100]}...")
        print(f"   🔗 {url}")

def main():
    print("=" * 60)
    print("        📰 Python News App 📰")
    print("=" * 60)
    print("1. Top Headlines (Technology)")
    print("2. Top Headlines (Business)")
    print("3. Top Headlines (Sports)")
    print("4. Search by keyword")
    print("0. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        data = get_top_headlines("technology")
        display_articles(data)
    elif choice == "2":
        data = get_top_headlines("business")
        display_articles(data)
    elif choice == "3":
        data = get_top_headlines("sports")
        display_articles(data)
    elif choice == "4":
        keyword = input("Enter keyword: ")
        data = get_news_by_keyword(keyword)
        display_articles(data)
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️  Get your free API key from https://newsapi.org/")
        print("   Then replace 'YOUR_API_KEY_HERE' with your key.")
    else:
        main()
