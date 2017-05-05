# import json, os, sys

# def handle_metadata(json_data, query):

# 	meta_results = []
# 	sq_list = query.split("in")[1:]

# 	sq=""
# 	# print sq_list
# 	for item in sq_list:
# 		sq += item

# 	print "SQ", sq


# 	# if sq.isdigit():
# 	# 	# print sq.isdigit()
# 	# 	# print "got here"
# 	for book in json_data:
# 		if book['pub_date']==sq:
# 			meta_results.append({
# 							'title': book['title'],
# 							'nid': "https://etc.princeton.edu/abcbooks/node/"+ book['nid_url'],
# 							})

# 		elif for loc in book['pub_location']:
# 				print "LOC ", loc
# 				if loc in sq:
# 					meta_results.append({
# 									'title': book['title'],
# 									'nid': "https://etc.princeton.edu/abcbooks/node/"+ book['nid_url'],
# 									})
# 	return meta_results

# 	# else:
# 	# 	for book in json_data:
# 	# 		for loc in book['pub_location']:
# 	# 			# print "LOC ", loc
# 	# 			if loc in sq:
# 	# 				meta_results.append({
# 	# 								'title': book['title'],
# 	# 								'nid': "https://etc.princeton.edu/abcbooks/node/"+ book['nid_url'],
# 	# 								})
# 	# 	# print query
# 	# 	# print "loc results ", meta_results
# 	# 	return meta_results

# json_data = []
# metadata_json = []

# for f in sys.argv[1:]:
# 	with open(f) as data_file:
# 		json_data = json.load(data_file)

# results = handle_metadata(json_data, "published in 1920")

# print results