import sys, json, os
# from handle_tags import handle_tags
# from handle_pages.py import handle_tags
# from handle_metadata import handle_metadata
# from handle_transcr import handle_transcr

####################################################################################

# counts total tags in book_title
def count_tags(book_title):
	global json_data

	# print "COUNT_TAGS book_title ", book_title
	tag_count = 0
	for book in json_data:
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['tags'] == None:
					continue
				for tag in page['tags']:
					tag_count += int(tag['count'])

	return tag_count

# counts total unique tags in book_title
def count_utags(book_title):
	global json_data

	book_dict = []	# to store already seen words
	tag_count = 0 
	for book in json_data:
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['tags'] == None:
					continue
				for tag in page['tags']:
					if tag['term'] not in book_dict:
						book_dict.append(tag['term'])
						tag_count+=1
	return tag_count

def tag_comp(comparison_char, query_num):
	global json_data

	book_list = []

	# print "Comparison: ", comparison_char
	if not query_num.isdigit():
		print "invalid number"
	else:
		for book in json_data:
			# print book['title']
			tag_count = 0
			for page in book['pages']:
				if page['tags'] == None: # no tags case
					continue
				for tag in page['tags']:
					tag_count+=tag['count']

			# > cases like 'tags > 100'
			if (comparison_char == '>' or comparison_char == 'greater' or comparison_char == 'more' or comparison_char == 'larger'):			
				# print tag_count
				if tag_count > int(query_num):
					# print "IT'S TRUE"
					book_list.append(book)

			# < cases like 'tags < 100'
			elif (comparison_char == '<' or comparison_char == 'less' or comparison_char == 'fewer' or comparison_char == 'smaller'):
				if tag_count < int(query_num):
					book_list.append(book)

			# = cases like 'tags = 100'
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal'):
				if tag_count == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	# for book in book_list:
	# 	print book['title']

	return book_list

def utag_comp(comparison_char, query_num):
	global json_data

	book_list = []

	if not query_num.isdigit():
		print "invalid number"
	else:
		for book in json_data:
			tag_count = 0
			book_dict = []
			for page in book['pages']:
				if page['tags'] == None: # no tags case
					continue
				for tag in page['tags']:
					if tag['term'] not in book_dict:
						book_dict.append(tag['term'])
						tag_count+=1
			# > cases like 'tags > 100'
			if (comparison_char == '>' or comparison_char == 'greater' or comparison_char == 'more' or comparison_char == 'larger'):
				if tag_count > int(query_num):
					book_list.append(book)

			# < cases like 'tags < 100'
			elif (comparison_char == '<' or comparison_char == 'less' or comparison_char == 'fewer' or comparison_char == 'smaller'):
				if tag_count < int(query_num):
					# print book['title']
					book_list.append(book)

			# = cases like 'tags = 100'
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal'):
				if tag_count == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	return book_list


def handle_tags(query):
	global json_data
	# print "query: ", query

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller']
	book_list = []

	if "unique" in query_words:
		# print "reached unique"
		for index, word in enumerate(query_words):
			# if word == '>' or word == '<' or word == '=':
			if word in kwords:
				# print "index + 1>>>>>> ", query_words[index+1]
				book_list = utag_comp(word, query_words[index+1])
	else:
		# print "reached normal"
		for index, word in enumerate(query_words):
			# print index, word
			# if word == ">" or word == "<" or word == "=":
			if words in kwords:
				# print "before tag_comp"
				# print "index + 1>>>>>> ", query_words[index+1]
				book_list = tag_comp(word, query_words[index+1])

	return book_list

####################################################################################

# counts total pages in book_title
def count_pages(book_title):
	global json_data
	
	page_count = 0
	for book in json_data:
		if book['title'].lower() == book_title.lower():
			if book['pages'] == None:
				return -1
			else:
				for page in book['pages']:
				# else:
				# 	for page in book['pages']:
					page_count+=1
	return page_count

def page_comp(comparison_char, query_num):
	global json_data

	book_list = []

	# print "Comparison: ", comparison_char
	if not query_num.isdigit():
		print "invalid number"
	else:
		for book in json_data:
			page_count = 0
			# for page in book['pages']:
			if book['pages'] == None: # no pages case
				continue
			else:
				for page in book['pages']:
					page_count+=1
			# > cases like 'pages > 100'
			if (comparison_char == '>' or comparison_char == 'greater' or comparison_char == 'more' or comparison_char == 'larger'):
				# print page_count
				if page_count > int(query_num):
					book_list.append(book)

			# < cases like 'pages < 100'
			elif (comparison_char == '<' or comparison_char == 'less' or comparison_char == 'fewer' or comparison_char == 'smaller'):
				if page_count < int(query_num):
					book_list.append(book)

			# = cases like 'pages = 100'
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal'):
				if page_count == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	# for book in book_list:
	# 	print book['title']

	return book_list


def handle_pages(query):
	global json_data

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller']
	book_list = []

	# print "reached normal"
	for index, word in enumerate(query_words):
		# print index, word
		# if word == ">" or word == "<" or word == "=":
		if word in kwords:	
			book_list = page_comp(word, query_words[index+1])

	return book_list

####################################################################################

# counts total transcr in book_title
def transcr_len(book_title):
	global json_data
	
	transcr_len = 0
	for book in json_data:
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['text'] == None:
					continue
				for transcr in page['text']:
					transcr_len+=len(transcr.split())
	return transcr_len

def transcr_comp(comparison_char, query_num):
	global json_data

	book_list = []

	# print "Comparison: ", comparison_char
	if not query_num.isdigit():
		print "invalid number"
	else:
		for book in json_data:
			# print book['title']
			transcr_len = 0
			for page in book['pages']:
				if page['text'] == None:
					continue
				for transcr in page['text']:
					transcr_len+=len(transcr.split())
			# > cases like 'transcr > 100'
			if (comparison_char == '>' or comparison_char == 'greater' or comparison_char == 'more' or comparison_char == 'larger' or comparison_char == 'longer'):
				if transcr_len > int(query_num):
					book_list.append(book)

			# < cases like 'transcr < 100'
			elif (comparison_char == '<' or comparison_char == 'less' or comparison_char == 'fewer' or comparison_char == 'smaller' or comparison_char == 'shorter'):
				if transcr_len < int(query_num):
					book_list.append(book)

			# = cases like 'transcr = 100'
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal'):
				if transcr_len == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	return book_list


def handle_transcr(query):
	global json_data

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller']
	book_list = []

	# print "reached normal"
	for index, word in enumerate(query_words):
		# print index, word
		# if word == ">" or word == "<" or word == "=":
		if word in kwords:
			book_list = transcr_comp(word, query_words[index+1])

	return book_list

####################################################################################

# handle metadata

####################################################################################

def handle_query(query):

	global json_data

	json_data = []
	path = '../json_files/'
	listing = os.listdir(path)
	for jsonfile in listing:
		json_fname = "../json_files/" + jsonfile
		with open(json_fname) as data_file:
			json_data.append(json.load(data_file))

	# print "JSON DATA ", json_data

	# splice raw query into multiple conditions if appropriate
	sub_queries = query.lower().split(" ")
	print ">>>>SUBQUERIES ", sub_queries

	# lists of key query terms
	tag_queries = ['tags', 'tag', 'terms', 'term']
	page_queries = ['page', 'pages']
	transcr_queries = ['transcription', 'text', 'words']
	metadata_queries = ['location', 'place', 'date', 'year', 'metadata']

	# for sub_q in sub_queries:
	# 	print "query word: ", sub_q

	# remove stopwords


	book_list = []

	# handle query according to key query terms in query
	for sub_q in sub_queries:
		if sub_q in tag_queries:
			book_list = handle_tags(query)
		elif sub_q in page_queries:
			book_list = handle_pages(query)
		elif sub_q in transcr_queries:
			book_list = handle_transcr(query)
		elif sub_q in metadata_queries:
			print "metadata query"
			# book_list = handle_metadata(query)
		else:
			# print "no category"
			continue

	book_results = []
	# print "BOOK LIST ", book_list['title']
	for book in book_list:
		# print "BOOK LIST ", book['title']
		book_results.append({
			'title': book['title'],
			'tag_count': count_tags(book['title']),
			'utag_count': count_utags(book['title']),
			'page_count': count_pages(book['title']),
			'transcr_len': transcr_len(book['title'])
			})

	return book_results

####################################################################################
# test main
def main():
	# load all json data
	global json_data 

	print "To exit, type \"exit\" or \"end\".\n"

	while True:
		raw_query = raw_input(">> Enter query: \n")	# prompt for queries

		if raw_query.lower() == "exit" or raw_query.lower() == "end":
			print "goodbye"
			break

		subqueries = raw_query.lower().split(",")	# if multiple queries

		book_list = []

		# print "subqueries: ", subqueries
		for raw_subquery in subqueries:
			# print "hi hi ", raw_subquery
			# bk_list = handle_query(raw_subquery)
			# if bk in book_list not in bk_list:
			# 	book_list.pop(bk)
			book_list = handle_query(raw_subquery)

		for book in book_list:
			# print book['title'], count_utags(book['title'])
			print book['title']
		print ""
		print len(book_list), " result(s)\n"


####################################################################################

# main()
