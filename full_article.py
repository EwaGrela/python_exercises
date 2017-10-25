"""
the goal of this exercise is to retrieve an article from a website and its text
"""
# first you import your libraries
import requests
from bs4 import BeautifulSoup
url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
# get the article and check what is the code - 200 means it is ok
r = requests.get(url)
#print r
# once you know you have access, get the whole page markup

text = r.text
#print text
# now, give it to be parsed by BS
soup = BeautifulSoup(text, "lxml")
content = soup.find_all("p")
#print content
pars = []
for par in content:
  reading = par.get_text()
  print reading
  pars.append(reading)


#print pars,
print type(pars)
pars = " ".join(pars).encode('utf-8').strip()
#print pars
print type(pars)

with open("full_art.txt", "w") as my_file:
  my_file.write(pars)

