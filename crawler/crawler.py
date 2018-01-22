import requests
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from pyquery import PyQuery 
import xml.etree.ElementTree as ET   

class ATTCrawler :
	def __init__(self) :
		response = requests.get("http://gocthugian.com.vn/truyen/t457/")
		pyQuery = PyQuery(response._content)

		tableChap = pyQuery('td.ChI a')
		for a in tableChap :
			print a.text, a.attrib["href"]
		print "hello"

