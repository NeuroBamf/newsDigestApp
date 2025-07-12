import feedparser
from newspaper import Article
import nltk
from datetime import datetime
from pathlib import Path
import subprocess
import os

nltk.download('punkt')

rss_feeds = {

    "NPR": "https://feeds.npr.org/1001/rss.xml",
    "AP News": "https://apnews.com/rss",
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml"
}

# Create output directory
output_dir = Path("news_digests")
output_dir.mkdir(exist_ok=True)

# Create file with today's date
today = datetime.now().strftime("%Y-%m-%d")
file_path = output_dir / f"Daily_News_Digest_{today}.txt"

# Collect the digest content
digest = []
digest.append(f"🗞️ Daily News Digest — {today}\n")

for source, url in rss_feeds.items():
    digest.append(f"\n🔷 {source.upper()}\n")

    feed = feedparser.parse(url)
    entries = feed.entries[:5]  # Top 5

    for entry in entries:
        article_url = entry.link

        try:
            article = Article(article_url)
            article.download()
            article.parse()
            article.nlp()
        except Exception:
            continue

        # Use date from entry
        pub_date_str = "Unknown"
        try:
            pub_struct = entry.published_parsed
            publish_datetime = datetime(*pub_struct[:6])
            pub_date_str = publish_datetime.strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass

        digest.append(f"{article.title}")
        digest.append(f"🕒 Published: {pub_date_str}")
        digest.append(article.summary)
        digest.append(f"🔗 Read more: {article_url}")
        digest.append("-" * 80)

# Write digest to file
file_path.write_text("\n".join(digest), encoding="utf-8")

# Automatically open the file
if os.name == 'posix':  # macOS/Linux
    subprocess.run(["open", file_path])
elif os.name == 'nt':  # Windows
    os.startfile(file_path)
else:
    print(f"Saved to {file_path} (please open manually)")
