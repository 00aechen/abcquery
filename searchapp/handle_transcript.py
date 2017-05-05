# counts total transcr in book_title
def transcr_len(json_data, book_title):
	# global json_data
	
	transcr_len = 0
	for book in json_data:
		if book['title'].lower() == book_title.lower():
			for page in book['pages']:
				if page['text'] == None:
					continue
				for transcr in page['text']:
					transcr_len+=len(transcr.split())
	return transcr_len

def transcr_comp(json_data, comparison_char, query_num):
	# global json_data

	book_list = []
	print "PLUS ONE ", query_num
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
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal' or comparison_char == 'with'):
				if transcr_len == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	return book_list


def handle_transcr(query, json_data):

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller', 'with']
	book_list = []

	# print "reached normal"
	for index, word in enumerate(query_words):
		# print index, word
		# if word == ">" or word == "<" or word == "=":
		if word in kwords:
			book_list = transcr_comp(json_data, word, query_words[index+1])

	return book_list