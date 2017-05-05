import sys, json, os
from handle_tags import handle_tags, count_tags, count_utags
from handle_pages import handle_pages
# from handle_metadata import handle_metadata
from search_titles import search_titles, search_tags, search_text
from handle_transcript import handle_transcr, transcr_len


####################################################################################

# handle metadata

####################################################################################


def handle_query(json_data, query):

	# global json_data

	# json_data = []
	metadata_json = []


	# lists of key query terms
	tag_queries = ['tags', 'tag', 'terms', 'term']
	page_queries = ['page', 'pages', 'pgs']
	transcr_queries = ['transcription', 'text', 'words', 'length', 'wc', 'word']
	metadata_queries = ['publication', 'location', 'place', 'date', 'year', 'metadata']


	# path = '../json_files/'
	# listing = os.listdir(path)
	# # print "LISTING ", listing
	# # for jsonfile in listing:
	# # 	json_fname = "../json_files/" + jsonfile
	# # 	# print "Print ", json_fname
	# # 	# print "abspath ", os.path.abspath(json_fname)
	# # 	with open(json_fname) as data_file:
	# # 		json_data.append(json.load(data_file))
	# json_fname = "../json_files/" + "metadata_mod.json"
	# with open(json_fname) as data_file:
	# 	json_data = json.load(data_file)

	# split received query into multiple queries (separated by a comma)

	query_list = query.lower().split(",")
	# print "QUERY_LIST ", query_list
	
	book_list = []
	json_options=json_data

	for qry in query_list:


		if (len(qry.split())==1):
			title_book_list = search_titles(json_options, qry)
			tag_book_list = search_tags(json_options, qry)
			text_book_list = search_text(json_options, qry)
			# for bk in text_book_list:
			# 	print "WHERE ARE YOU ", bk['title']
			json_options = title_book_list

		# remove stopwords
		filtered_query = qry.lower()
		# print "QUERRRRRYYY ", filtered_query
		stopwrds = ['than', 'as']
		# for q in sub_queries:
		# 	print "!!!!!! ", q
		# 	if q in stopwrds:
		# 		print "YES", q
		# 		sub_queries.replace(q, '')

		# print "FILTERED ", sub_queries

		# splice raw query into multiple conditions if appropriate
		raw_sub_queries = qry.lower().split(" ")
		print ">>>>SUBQUERIES ", raw_sub_queries

		sub_queries=raw_sub_queries[:]
		for q in raw_sub_queries:
			# print q
			if q in stopwrds:
				sub_queries.remove(q)

		# print "FILTERED ", sub_queries

		

		# for sub_q in sub_queries:
		# 	print "query word: ", sub_q

		# print "QUERRRRRYYY ", query
		# # remove stopwords
		# sub_queries = query
		# stopwrds = ['than', 'as']
		# for q in sub_queries:
		# 	print "!!!!!! ", q
		# 	if q in stopwrds:
		# 		print "YES", q
		# 		sub_queries.replace(q, '')

		# print "FILTERED ", sub_queries

		filtered_query = ""
		for sq in sub_queries:
			filtered_query +=sq
			filtered_query +=" "
		# print "HALLELUJAH ", filtered_query		


		# if sq not in tag_queries and sq not in page_queries and sq not in transcr_queries:
		# 	return book_list

		# handle query according to key query terms in query
		for sub_q in raw_sub_queries:
			# for b in json_options:
			# 	print "loop top ", b['title']
			# 	print len(json_options)

			if sub_q in tag_queries:
				book_list = handle_tags(filtered_query, json_options)
			elif sub_q in page_queries:
				book_list = handle_pages(filtered_query, json_options)
			elif sub_q in transcr_queries:
				book_list = handle_transcr(filtered_query, json_options)
			# elif sub_q in metadata_queries:
			# 	# print "metadata query"
			# 	book_list = handle_metadata(json_options, filtered_query)
			else:
				continue
			json_options = book_list

		# 			for b in json_options:
		# 			print "another title ", b['title']
		# 			print len(json_options)

		# for b in json_options:
		# 	print "final json_options ", b['title']
		# 	print len(json_options)

	book_results = []
	# print "BOOK LIST ", book_list['title']
	for book in json_options:
		# print "BOOK LIST ", book['title']
		book_results.append({
			'title': book['title'],
			'img_url': book['cover_img'],
			'nid_url': book['nid_url'],
			'tag_count': count_tags(json_data, book['title']),
			'utag_count': count_utags(json_data, book['title']),
			'page_count': book['num_pages'],
			'transcr_len': transcr_len(json_data, book['title']),
			'pub_date': book['pub_date'],
			'pub_location': book['pub_location'],
			})

	return book_results

####################################################################################
# test main
def main():
	# load all json data
	# global json_data 

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
