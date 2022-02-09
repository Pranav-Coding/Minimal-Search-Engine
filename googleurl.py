from googlesearch import search


def genlinks(query):
	links = []
	for i in search(query, tld='com' ,lang='en', num=10, start=0, stop=15, pause=2.0):
		links.append(i)
	return links
