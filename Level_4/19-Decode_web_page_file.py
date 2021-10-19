# 19) Decode a web page 2 (Split to read a file)

# Using the library request and beautiful soup on the following site:
# https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture
# Print the article in the screen so you can read it without having to click any buttons

import requests
from bs4 import BeautifulSoup
import textwrap

# makes the request of the website
base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)

# returns all the HTML from the site requested
soup = BeautifulSoup(r.text)

# returns all text inside under tag "p"
# textwrap.wrap limit the lenght of the string
for elem in soup.find_all("p"):
  print("\n".join(textwrap.wrap(elem.text,80)))
  print("\n")