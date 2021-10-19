# 17) Decode a Web Page

# Use BeautifulSoup and request package of Python
# Print out all the articles titles of the New York Times homepage

import requests
from bs4 import BeautifulSoup

# makes the request of the website
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)

# returns all the HTML from the site requested
soup = BeautifulSoup(r.text)

# will return all tags of this class
for story_heading in soup.find_all(class_="story-wrapper css-1rroodt"):
    if story_heading.a:
        print(story_heading.a.text)
