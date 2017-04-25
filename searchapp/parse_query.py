def parse_query():
	global json_copy

	# split query into list of sub-queries (discarding first empty one)
	sub_queries = self.path.lower().split("/")[1:]

	distr_codes = ['la', 'sa', 'ha', 'em', 'ec', 'qr', 'stl', 'stn']	# distribution codes
	class_weekdays = ['m', 't', 'w', 'th', 'f', 'mw', 'mwf', 'tth', 'twth', 'mtwth', 'mtwthf'] # class days

	# LOOP TO GO THROUGH ALL THE SUB-QUERIES
	for index, sub_q in enumerate(sub_queries):
		selected = []

		# check distribution codes
		if sub_q in distr_codes:
			for course in json_copy:
				if len(course["area"]) > 0:
					if course["area"].lower() == sub_q:
						selected.append(course)
		# check days of the week
		elif sub_q in class_weekdays:
			for course in json_copy:
				if len(course["classes"]) > 0:
					# print course["classes"][0]["days"]
					if course["classes"][0]["days"].lower() == sub_q:
						selected.append(course)
		elif len(sub_q) == 3:
			# check departments
			if sub_q.isalpha():
				for course in json_copy:
					contains = False
					for listing in course["listings"]:
						if listing["dept"].lower() == sub_q:
							contains = True
					if contains:
						selected.append(course)
			# check course numbers
			elif sub_q.isdigit():
				# print "loop"
				for course in json_copy:
					contains = False
					for listing in course["listings"]:
						if int(listing["number"]) == int(sub_q):
							contains = True
					if contains:
						selected.append(course)
		# re sub-queries
		elif len(sub_q) > 3:
			for course in json_copy:
				time_bool = False
				title_bool = False
				prof_bool = False
				bldg_bool = False
				room_bool = False
				for section in course["classes"]:
					if re.search(sub_q, section["starttime"].split(" ")[0]) or re.search(sub_q, section["endtime"].split(" ")[0]):
						time_bool = True
					if re.search(sub_q, section["bldg"].lower()):
						bldg_bool = True
					if re.search(sub_q, section["roomnum"].lower()):
						room_bool = True
				for prof in course["profs"]:	
					if re.search(sub_q, prof["name"].lower()):
						prof_bool = True
				if re.search(sub_q, course["title"].lower()):
					title_bool = True
				if (time_bool or title_bool or prof_bool or bldg_bool or room_bool):
					selected.append(course)
		else:
			json_copy = []

		json_copy = selected

	if len(json_copy) == 0:
		self.wfile.write("\n")
	else :# print the courses that match the query
		for course in json_copy:
			course_str = ""	# empty string
			# CourseNumber
			if len(course["listings"]) > 1:
				for index, listing in enumerate(course["listings"]):
					course_str += listing["dept"]
					course_str += " "
					course_str += listing["number"]
					if (index < len(course["listings"])-1):
						course_str += "/"
			else:
				course_str += course["listings"][0]["dept"]
				course_str += " "
				course_str += course["listings"][0]["number"]
			# Area
			if (course["area"] != ""):
				course_str += " "
				course_str += course["area"]
			if len(course["classes"]) > 0:
				# Section
				if (course["classes"][0]["section"] != ""):
					course_str += " "
					course_str += course["classes"][0]["section"]
				# Day
				if (course["classes"][0]["days"] != ""):
					course_str += " "
					course_str += course["classes"][0]["days"]
				# Time
				course_str += " "
				course_str += course["classes"][0]["starttime"].split(" ")[0]
				course_str += "-"
				course_str += course["classes"][0]["endtime"].split(" ")[0]
			# Title
			if (course["title"] != ""):
				course_str += " "
				course_str += course["title"]
			# Prof
			if (len(course["profs"]) > 0):
				course_str += " "
				if len(course["profs"]) > 1:
					for index, listing in enumerate(course["profs"]):
						course_str += listing["name"]
						if (index < len(course["profs"])-1):
							course_str += "/"
				else:
					course_str += course["profs"][0]["name"]
			if len(course["classes"]) > 0:
				# Building
				if (course["classes"][0]["bldg"] != ""):
					course_str += " "
					course_str += course["classes"][0]["bldg"]
				# Room
				if (course["classes"][0]["roomnum"] != ""):
					course_str += " "
					course_str += course["classes"][0]["roomnum"]
			# write each course
			self.wfile.write(course_str.encode('utf8'))
			self.wfile.write("\n")