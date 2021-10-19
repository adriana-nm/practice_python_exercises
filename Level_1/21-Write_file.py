# 21) Write a file

# Extract the titles of the New York Times homepage
# Save the titles in a new file
# Request the user to name the file

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

filename = input('Introduce name of the file:')

with open(filename,'w') as file:
    file.write("\n")
    for story_heading in soup.find_all(class_="story-wrapper css-1rroodt"):
        if story_heading.a:
            file.write(story_heading.a.text)
            file.write("\n")
