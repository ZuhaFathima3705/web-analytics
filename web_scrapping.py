import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt

print("===== WEB SCRAPING + ANALYSIS =====\n")

# Step 1: Fetch Website
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract Headlines
titles = soup.find_all("a")

words = []

print("Latest Headlines:\n")

for t in titles[:20]:
    text = t.text.strip()
    if text:
        print("-", text)
        words.extend(text.lower().split())

# Step 4: Keyword Frequency Analysis
word_count = Counter(words)

print("\nTop Keywords:")
for word, count in word_count.most_common(5):
    print(word, "->", count)

# Step 5: Data Visualization
top_words = word_count.most_common(5)

w = [i[0] for i in top_words]
c = [i[1] for i in top_words]

plt.bar(w, c)
plt.title("Top Keywords in News")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
