def page_comp(json_data, comparison_char, query_num):
	# global json_data

	book_list = []
	print "PLUS ONE ", query_num
	# print "Comparison: ", comparison_char
	if not query_num.isdigit():
		print "invalid number"
	else:
		for book in json_data:
			# page_count = 0
			# # for page in book['pages']:
			# if book['pages'] == None: # no pages case
			# 	continue
			# else:
			# 	for page in book['pages']:
			# 		page_count+=1

			page_count = int(book["num_pages"])

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
			elif (comparison_char == '=' or comparison_char == 'same' or comparison_char == 'equals' or comparison_char == 'equal' or comparison_char == 'with'):
				if page_count == int(query_num):
					book_list.append(book)

			# invalid comparison
			else:
				sys.stdout.write('illegal comparison character')

	# for book in book_list:
	# 	print book['title']

	return book_list


def handle_pages(query, json_data):
	# global json_data

	query_words = query.split(" ")
	kwords = ['>', '<', '=', 'longer', 'larger', 'greater', 'more', 'equals', 'equal', 'same', 'shorter', 'less', 'fewer', 'smaller', 'with']
	book_list = []

	# print "reached normal"
	for index, word in enumerate(query_words):
		# print index, word
		# if word == ">" or word == "<" or word == "=":
		if word in kwords:	
			book_list = page_comp(json_data, word, query_words[index+1])

	return book_list