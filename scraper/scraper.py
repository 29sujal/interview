import requests
import xml.etree.ElementTree as ET
import schedule
import time
import json
import datetime
import os

BASE_URL = "https://news.google.com/rss/search?q=ai"
KEYWORDS = ["ai"]
WEBHOOK_URL = "http://localhost:3000/webhook"
SEEN_FILE = "seen.json"


if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, 'r') as f:
        seen_urls = set(json.load(f))
else:
    seen_urls = set()

def save_seen():
    with open(SEEN_FILE, 'w') as f:
        json.dump(list(seen_urls), f)

def scrape_headlines():
    print("\nChecking Google News for AI-related articles...")
    try:
        res = requests.get(BASE_URL, timeout=10)
        root = ET.fromstring(res.content)

        items = root.findall(".//item")
        print(f"Found {len(items)} articles")

        for item in items:
            title = item.find("title").text
            url = item.find("link").text

            print(f"→ {title}")

            if not any(k in title.lower() for k in KEYWORDS):
                continue
            if url in seen_urls:
                continue

            payload = {
                "title": title,
                "url": url,
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
            }

            try:
                response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                print(f"Sent: {title}")
                seen_urls.add(url)
                save_seen()
            except Exception as e:
                print("Webhook Error:", e)

    except Exception as e:
        print("Failed to fetch news:", e)


schedule.every(1).minutes.do(scrape_headlines)

if __name__ == "__main__":
    scrape_headlines()
    while True:
        schedule.run_pending()
        time.sleep(1)
