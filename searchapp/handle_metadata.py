import json, os, sys

def handle_metadata(json_data, query):

	loc_results = []
	sq = query.split()

	for book in json_data:
		print book['pub_location']
		for loc in book:
			if loc in sq:
				loc_results.append(book)

	print loc_results
	return loc_results

json_data = []
metadata_json = []

for f in sys.argv[1:]:
	with open(f) as data_file:
		json_data.append(json.load(data_file))

results = handle_metadata(json_data, "New York")

print results