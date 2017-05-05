# counts total tags in book_title
def count_tags(json_data, book_title):

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
def count_utags(json_data, book_title):
	# global json_data

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

def tag_comp(json_data, comparison_char, query_num):
	# global json_data

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

def utag_comp(json_data, comparison_char, query_num):
	# global json_data

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
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal' or comparison_char == 'with'):
				if tag_count == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	return book_list


def handle_tags(query, json_data):
	# global json_data

	# print "query: ", query

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller', 'with']
	book_list = []

	if "unique" in query_words:
		# print "reached unique"
		for index, word in enumerate(query_words):
			# if word == '>' or word == '<' or word == '=':
			if word in kwords:
				# print "index + 1>>>>>> ", query_words[index+1]
				book_list = utag_comp(json_data, word, query_words[index+1])
	else:
		# print "reached normal"
		for index, word in enumerate(query_words):
			# print index, word
			# if word == ">" or word == "<" or word == "=":
			if word in kwords:
				# print "before tag_comp"
				# print "index + 1>>>>>> ", query_words[index+1]
				book_list = tag_comp(json_data, word, query_words[index+1])

	return book_list