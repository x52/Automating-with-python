import sys,requests
from bs4 import BeautifulSoup
from googlesearch import search

# to search
print("Enter the song name and artist")
song_name = input()

query = song_name + " metrolyrics"
for j in search(query, tld="com", num=1, stop=1, pause=2):
	url = j

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lyrics = ""
for raw in soup.find_all('p',class_='verse'):
	#lyrics.append(raw.get_text())
	lyrics += raw.get_text()

print("\n\n\n\n\n")
print("Lyrics for ==============>" + song_name)
print("\n\n")
print(lyrics)

