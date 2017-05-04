import sys, json, os, pprint

pp = pprint.PrettyPrinter(indent=4)

json_data = []
metadata_json = []

for f in sys.argv[1:]:
	with open(f) as data_file:
		json_data.append(json.load(data_file))
# pp.pprint(json_data)

for bk in json_data:
	metadata_json.append({
		"title": bk["title"],
		"pub_location": [],
		"pub_date": "",
		})
pp.pprint(metadata_json)

# with open("json_files/metadata.txt", 'w') as t_file:
# 	t_file.write(metadata_json)