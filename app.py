import os.path
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

pageHtml = ""

def loadCapitals():
	try:
		fname = 'capitals.html'
		global pageHtml
		if os.path.isfile(fname):
			with open(fname, 'r', encoding='utf-8') as f:
				pageHtml = f.read()
			print('ok')
		else:
			print('file not found.')

	except Exception as e:
		print('cant open file: ', e)
	
def start():
	loadCapitals()
	while True:
		country = input('What is the capital city of: ')
		print(findCapital(country))

def downloadCapitals():
	try:
		response = urllib2.urlopen('https://www.countries-ofthe-world.com/capitals-of-the-world.html')
		respBytes = response.read()
		global pageHtml
		pageHtml = respBytes.decode("utf-8")
		with open('capitals.html', 'w', encoding='utf-8') as f:
			f.write(pageHtml)
		print('ok')
	except Exception as e:
		print('error:', e)
	
	
def findCapital(country):
	idx = pageHtml.lower().find(country.lower())
	if idx >= 0:
		endCountryIdx = pageHtml.lower().find('<td>', idx)
		if endCountryIdx > idx:
			endCityIdx = pageHtml.lower().find('</td>', endCountryIdx)
			startCityIdx = (endCountryIdx + 4)
			cityHtml = pageHtml[startCityIdx:endCityIdx]
			return cityHtml
	else:
		return 'nothing found.'

