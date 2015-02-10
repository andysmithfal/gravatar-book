import os, sys
from urllib2 import urlopen
import hashlib, re, urllib
from json import load 

class Book():
	def __init__(self, title, summary, book_id, isbn10, avatar_hash, avatar_url):
		self.title = title
		self.summary = summary
		self.book_id = book_id
		self.isbn10 = isbn10
		self.avatar_hash = avatar_hash
		self.avatar_url = avatar_url


def generateGravs(avatar_hash, typeof):
	print "Generating " + typeof + "Url..."
	url = "http://www.gravatar.com/avatar/"+avatar_hash+"?s=300&d="+typeof+"&r=g"
	print url
	return url 

def getHashUrl(aobject):
	b = aobject
	avatar_hash = b.avatar_hash

	identicon = generateGravs(avatar_hash, "identicon")
	retro = generateGravs(avatar_hash, "retro")
	monster = generateGravs(avatar_hash, "monsterid")

	urllib.urlretrieve(identicon, 'img/raw/'+b.book_id+'_identicon.png')
	urllib.urlretrieve(retro, 'img/raw/'+b.book_id+'_retro.png')
	urllib.urlretrieve(monster, 'img/raw/'+b.book_id+'_monster.png')

	print "Saved images to folder"
	return identicon

def downloadBook(barcode):
	apikey = '2QUS7QQR'
	apiurl = 'http://isbndb.com/api/v2/json/'+apikey+'/book/'+ barcode
	
	print apiurl

	response = urlopen(apiurl)
	json = load(response)

	try:
		print json['data']
	except KeyError:
		print "Book does not exist in database. Please try another."
		return
	else:		
		for book in json['data']:
			
			# avatar_hash = hashlib.md5(book['isbn10'].encode('utf-8')).hexdigest()
			avatar_hash = book['isbn10']

			b = Book(book['title'], book['summary'], book['book_id'], book['isbn10'], avatar_hash, '')
			
			b.avatar_url = getHashUrl(b)
			
			print b.title
			print b.summary
			print "Avatar hash: ", b.avatar_hash

			return b

a = True

while a is True:
	book = raw_input('Book Number: ')

	if book == 'exit':
		sys.exit()
	elif len(book) < 10:
		print "Must be book barcode or ISBN 10 or 13 characters long"
	else:
		try:
			book = int(book)
		except ValueError:
			print "Must be a book barcode/ISBN excluding letters or dashes"
		else:
			book = str(book)
			downloadBook(book)






