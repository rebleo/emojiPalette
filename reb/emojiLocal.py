#learning to scrape: http://www.unicode.org/emoji/charts/full-emoji-list.html
from bs4 import BeautifulSoup
import sys

#open the html page, read it & close it
emoRaw = open("page_content.html")
emoRead = emoRaw.read()
emoRaw.close()

# print emoRead
#soup the emojiData
emoSoup = BeautifulSoup(emoRead, "html.parser")

# print emoSoup.prettify()
emoTable = emoSoup.find_all('table')

##break the table up by html tag 'tr' into rows
rows = emoTable[0].find_all('tr')

for row in rows: 
	cols = row.find_all('td')
	# emojiRow.append(cols)

##find the 4 coloumn in the data
	try:
		print cols[4]
	except: IndexError
