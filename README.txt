📰 Daily News Digest App
This Python application summarizes the top recent news stories from NPR, AP News, and BBC, focusing on articles published within the last two days. It generates a neatly formatted .txt digest, which automatically opens on your screen each morning at 8 AM (configurable via cron or launchd). 

📌 What the App Does
* Scrapes the top 5 articles from NPR, AP News, and BBC RSS feeds.
* Filters for articles published today or the day before.
* Uses Natural Language Processing (NLP) to extract key summaries.
* Exports the results to a .txt file, saved with the current date.
* Automatically opens the digest on your computer when generated.

🛠 Technologies Used
* Python 3
* newspaper3k – for article parsing and summarization
* feedparser – for parsing RSS feeds
* nltk – for natural language processing
* lxml_html_clean - clean up HTML content
* macOS/Linux automation via cron or launchd

🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/NeuroBamf/news-digest-app.git
cd news-digest-app

2. Create and Activate a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate  
# On Windows use: .venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the App Manually (Optional)
python news_digest.py

⏰ Auto Run at 8AM Daily (macOS/Linux)
1. Open your crontab:
crontab -e
2. Add this line:
0 8 * * * /path/to/your/project/.venv/bin/python /path/to/your/project/news_digest.py
🔍 Replace /path/to/your/project/ with the actual full path on your system.Use which python inside your .venv to find the correct Python path. 

📁 Output Example
A file will be created like:
news_digests/Daily_News_Digest_2025-07-11.txt
Each digest includes:
* 📰 Article Title
* 🕒 Published Timestamp
* ✂️ NLP-generated Summary
* 🔗 Link to Full Article

🎯 Future Goals
* Build a UI-based version for macOS, Windows, and Linux.
* Develop a mobile version (iOS & Android).
* Support user preferences by category or source.
* Add email or push notifications for digests.

✅ Requirements
Add these to your requirements.txt:
feedparser
newspaper3k
nltk
lxml_html_clean
Note: The script automatically downloads NLTK's punkt tokenizer if not found.

🙌 About
Hope you like it. Developed by C. Howard