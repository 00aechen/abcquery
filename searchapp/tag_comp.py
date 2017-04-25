def tag_comp(comparison_char, query_num):
	global json_data

	book_list = []

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
		sys.stderr.write('illegal comparison character')



