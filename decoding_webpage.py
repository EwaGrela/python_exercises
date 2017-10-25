"""
this is the first time I am using bs4 to crawl a website - my goal was to find all headers with specific class
"""

import requests
from bs4 import BeautifulSoup

url ="https://www.nytimes.com/"
r = requests.get(url)
content = r.text
page = BeautifulSoup(content, "lxml")
headers = page.find_all(class_="story-heading")
print headers
for header in headers:
  text = header.get_text()
  print text
