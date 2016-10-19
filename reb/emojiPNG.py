#learning to scrape: http://www.unicode.org/emoji/charts/full-emoji-list.html
from bs4 import BeautifulSoup
import sys


emoRaw = open("page_content.html")
# notes = open('netNotes.txt')
emoRead = emoRaw.read()
emoRaw.close()

# print emoRead
emoSoup = BeautifulSoup(emoRead, "html.parser")

# print emoSoup.prettify()
emoTable = emoSoup.find_all('table')


emojiData = []



##break the table up by rows
rows = emoTable[0].find_all('tr')

##break those rose by columns (18 count)
for row in rows: 
	cols = row.find_all('td')
	# emojiRow.append(cols)
##the 4th row is the first with data links to emoji images
	try:
		for items in cols[4].find_all('img'):
			emojiData.append(items.get('src'))
	except: IndexError
print emojiData