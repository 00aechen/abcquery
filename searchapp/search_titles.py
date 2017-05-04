# search through the titles first
# 	if books returned list them
# then tags
# 	dict tuple: [{title, [pages]}]
# 	list pages the tags show up on 



def search_titles(json_data, query):
	# rm stopwords
	pquery = query
	stopwords = ['the', 'a', 'of', 'and', 'or', 'an']
	for sw in pquery.split():
		if sw in stopwords:
			pquery.replace(sw, "")

	book_matches = []
	for bk in json_data:
		if word in pquery in book['title'].lower():
			book_matches.append(book['title'])

	return book_matches

def search_tags(json_data, query):
	tag_results=[]

	for book in json_data:
		for pg in book['pages']:
			for tag in pg['tags']:
				if tag['term'].lower()==query:
					if tag['term'] not in tag_results['tag']:
						tag_results.append({
							'tag' : tag['term'],
							'tag-pages': [pg['title']]
							})
					else:
						tag_results['term']