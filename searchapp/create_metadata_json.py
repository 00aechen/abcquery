import sys, json, os, pprint

pp = pprint.PrettyPrinter(indent=4)

json_data = []
metadata_json = []

for f in sys.argv[1:]:
	with open(f) as data_file:
		json_data.append(json.load(data_file))
# pp.pprint(json_data)

# for bk in json_data:
# 	metadata_json.append({
# 		"title": bk["title"],
# 		"nid_url": "https://etc.princeton.edu/abcbooks/node/",
# 		"pub_location": [],
# 		"pub_date": "",
# 		})
# pp.pprint(metadata_json)

# with open("metadata.txt", 'w') as t_file:
# 	json.dump(metadata_json, t_file)

with open("metadata.json") as md_file:
	metadata_json = json.load(md_file)

# pp.pprint(metadata_json)

for book in json_data:
	for info in metadata_json:
		if info['title'] == book ['title']:
			book['nid_url'] = info['nid_url']
			book['pub_date'] = info['pub_date']
			book['pub_location'] = info['pub_location']

# pp.pprint(json_data)

with open("metadata_mod.json", 'w') as t_file:
 	json.dump(json_data, t_file)