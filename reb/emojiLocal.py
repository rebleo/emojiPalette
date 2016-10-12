#learning to scrape: http://www.unicode.org/emoji/charts/full-emoji-list.html
from bs4 import BeautifulSoup
import sys

emoRaw = open("page_content.html")
emoRead = emoRaw.read()
emoRaw.close()

# print emoRead

emoSoup = BeautifulSoup(emoRead, "html.parser")

# print emoSoup.prettify()
emoTable = emoSoup.find_all('table')


##these are to hold the categories from the table
number = []
code = []
name = []
date = []
keywords = []
chars = []

andr = []
test = []

##break the table up by rows
rows = emoTable[0].find_all('tr')


for row in rows:
##This all the text data, put into arrays
	digit = row.find_all('td', { "class" : "rchars"})
	number.append(digit)
	
	uni = row.find_all('td', { "class" : "code"})
	code.append(uni)
	# print uni

	person = row.find_all('td', { "class" : "name"})
	name.append(person)
	# print name

	age = row.find_all('td', { "class" : "age"})
	date.append(age)

	adjectives = row.find_all('td', { "class" : "name"})
	keywords.append(adjectives)

test.append(number[1])
test.append(code[1])
test.append(name[1])
test.append(date[1])
test.append(keywords[1])
print test

#emoji-image part of table!!!!!
#THIS RETURNS UNICODE CODES!
	# emoji = row.find_all('td', { "class" : "chars"})
	# print emoji

	# THIS IS WHERE SHIT WILL GET MORE COMPLICATED...
	# emoji = row.find_all('td', { "class" : "andr"})
	# andr.append(emoji)
