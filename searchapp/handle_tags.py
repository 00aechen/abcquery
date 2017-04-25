import sys, json

# counts total tags in book_title
def count_tags(book_title):
	global json_data

	for book in json_data:
		tag_count = 0
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['tags'] == None:
					continue
				for tag in pages['tags']:
					tag_count+=tag['count']
	return tag_count

# counts total unique tags in book_title
def count_utags(book_title):
	global json_data

	book_dict = []	# to store already seen words

	for book in json_data:
		tag_count = 0
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['tags'] == None:
					continue
				for tag in pages['tags']:
					if tag['term'] not in book_dict:
						book_dict.append(tag['term'])
						tag_count+=1
	return tag_count

def tag_comp(comparison_char, query_num):
	global json_data

	book_list = []

	sys.stdout.write(query_num)

	if not query_num.isdigit():
		print "invalid number"
	else:
		# > cases like 'tags > 100'
		if (comparison_char == '>'):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=tag['count']
				if tag_count > query_num:
					book_list.append(book)

		# < cases like 'tags < 100'
		elif (comparison_char == '<'):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=tag['count']
				if tag_count < query_num:
					book_list.append(book)

		# = cases like 'tags = 100'
		elif (comparison_char == '='):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=tag['count']
				if tag_count == query_num:
					book_list.append(book)

		# invalid comparison
		else:
			sys.stdout.write('illegal comparison character')

def utag_comp(comparison_char, query_num):
	global json_data

	book_list = []

	if not query_num.isdigit():
		print "invalid number"
	else:
		# > cases like 'tags > 100'
		if (comparison_char == '>'):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=1
				if tag_count > query_num:
					book_list.append(book)


		# < cases like 'tags < 100'
		elif (comparison_char == '<'):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=1
				if tag_count < query_num:
					book_list.append(book)

		# = cases like 'tags = 100'
		elif (comparison_char == '='):
			# count tags for each book in json_data
			for book in json_data:
				tag_count = 0
				for page in book['pages']:
					if page['tags'] == None: # no tags case
						continue
					for tag in page['tags']:
						tag_count+=1
				if tag_count == query_num:
					book_list.append(book)

		# invalid comparison
		else:
			sys.stdout.write('illegal comparison character')


def handle_tags(query):
	global json_data
	print "query: ", query

	query_words = query.split(" ")

	print "query_words: ", query_words

	print "reached here"

	if "unique" in query_words:
		print "reached unique"
		for index, word in enumerate(query_words):
			if word == '>' or word == '<' or word == '=':
				print "index + 1>>>>>> ", query_words[index+1]
				utag_comp(word, query_words[index+1])
	else:
		print "reached normal"
		for index, word in enumerate(query_words):
			# print index, word
			if word == ">" or word == "<" or word == "=":
				print "before tag_comp"
				print "index + 1>>>>>> ", query_words[index+1]
				tag_comp(word, query_words[index+1])



