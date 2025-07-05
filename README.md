### ✅ `README.md`

```markdown
# 📰 Real-Time News Headline Scraper and Notifier

A real-time AI news monitoring system that scrapes Google News RSS for articles related to **"AI"** and sends instant notifications to a webhook built using **Express.js**.

---

## 📌 Features

- 🔁 Scrapes Google News RSS every minute
- 🔎 Filters headlines containing the keyword **"AI"**
- 🚫 Avoids duplicate notifications using a `seen.json` file
- 📤 Sends article details (title, URL, timestamp) to a webhook
- 🗃 Logs all notifications in `notifications.log`
- ⚙ Built with Python, RSS, `requests`, `schedule`, `xml.etree`, and Node.js (Express)

---

## 🛠️ Tech Stack

- **Python** (scraper)
- **Express.js** (webhook server)
- **Google News RSS Feed** (source)
- **Node.js File System** for logging

---

## 📂 Project Structure

```

interview/
│
├── scraper/
│   └── scraper.py           # Python script that scrapes and sends notifications
│   └── seen.json            # Stores URLs of already sent articles
│
├── server/
│   └── index.js             # Webhook endpoint using Express.js
│   └── notifications.log    # Logs received articles

````

---

## 🚀 How It Works

1. The scraper (`scraper.py`) fetches latest articles from [Google News RSS](https://news.google.com/rss/search?q=ai)
2. Filters articles with keywords like **"AI"**
3. Sends unseen articles to `http://localhost:3000/webhook`
4. The webhook (`index.js`) logs and prints them in real time

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/29sujal/interview.git
cd interview
````

### 2. Start the Webhook Server

```bash
cd server
npm install
node index.js
```

It will start listening on: `http://localhost:3000/webhook`

### 3. Run the Scraper

```bash
cd scraper
pip install -r requirements.txt
python scraper.py
```

> The scraper checks for new articles every 1 minute.

---

## 📦 Dependencies

### Python

* `requests`
* `schedule`

### Node.js

* `express`
* `cors`
* `fs`

---

## ✅ Sample Output

```bash
Checking Google News for AI-related articles...
Found 25 articles
→ OpenAI launches GPT-5 model
Sent: OpenAI launches GPT-5 model
```

Webhook server:

```
OpenAI launches GPT-5 model
    ↳ https://example.com/openai-gpt5 @ 2025-07-05T08:45:00Z
```

---


