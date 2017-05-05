# search through the titles first
# 	if books returned list them
# then tags
# 	dict tuple: [{title, [pages]}]
# 	list pages the tags show up on 


import sys, json, os, pprint

pp = pprint.PrettyPrinter(indent=4)

# json_data = []

# for f in sys.argv[1:]:
# 	with open(f) as data_file:
# 		json_data.append(json.load(data_file))

def search_titles(json_data, query):
	# rm stopwords
	pquery = query
	stopwords = ['the', 'a', 'of', 'and', 'or', 'an']
	# punctuation = ['\'', '\"']
	for sw in pquery.split():
		if sw in stopwords:
			pquery.replace(sw, "")
	# for p in pquery:
	# 	print p
	# 	if p in punctuation:
	# 		pquery.replace(p, "")

	# print "THIS IS PQUERY ", pquery

	book_matches = []
	for bk in json_data:
		for word in pquery.split():
			# print "WORD ", word
			if word.lower() in bk['title'].lower():
				# print bk['title'].lower().encode("utf8", "ignore")
				book_matches.append(bk)

	return book_matches

def search_tags(json_data, query):
	tag_results=[]

	# print json_data
	for book in json_data:
		# print book
		# print "PAGES ", book['pages']
		for pg in book['pages']:
			# print "PPPPPGGGG ", pg
			if pg['tags'] == None:
				continue;
			else: 
				for tag in pg['tags']:
					# print tag['term']
					if str(tag['term']).lower()==query:
						if tag['term'] not in tag_results:
							tag_results.append({
								'title': pg['title'],
								'nid': "https://etc.princeton.edu/abcbooks/node/"+ pg['nid'],
								})

	print tag_results
	return tag_results


def search_text(json_data, query):
	text_results=[]

	# print json_data
	for book in json_data:
		# print book
		# print "PAGES ", book['pages']
		for pg in book['pages']:
			# print "PPPPPGGGG ", pg
			if pg['text'] == None:
				continue;
			else: 
				for wrd in pg['text'].split():
					# print tag['term']
					if wrd.lower()==query:
						if wrd not in text_results:
							text_results.append({
								'title': pg['title'],
								'nid': "https://etc.princeton.edu/abcbooks/node/"+ pg['nid'],
								})
	return text_results

def main():
	json_data = []
	results=[]

	for f in sys.argv[1:-1]:
		with open(f) as data_file:
			# print f
			json_data.append(json.load(data_file))

	# pp.pprint(json_data)

	results = search_tags(json_data, "racism")
	results2 = search_titles(json_data, "aBc")
	results3 = search_text(json_data, 'pie')
	# pp.pprint("There's something going on.")
	# pp.pprint(results)
	# pp.pprint(results3)

main()
