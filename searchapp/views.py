from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from handle_query import handle_query
from search_titles import search_tags, search_text
import os, sys, json

# Create your views here.
def index(request):
	template = loader.get_template('searchapp/index_2.html')
	
	# # every time the index page is accessed, load json (edit later)
	# j_data = []
	# with open("searchapp/ABCAnAlphabet.json") as data_file:
	# 	j_data.append(json.load(data_file))

	context = {
		'Title': 'Index Page',
	}
	# print "I got to my index page!"
	return HttpResponse(template.render(context, request))

	
def search(request):
	result_list = []
	tag_result_list = []
	text_result_list = []

	path = '../json_files/'
	listing = os.listdir(path)
	json_fname = "../json_files/" + "metadata_mod.json"
	with open(json_fname) as data_file:
		json_data = json.load(data_file)

	if request.method == 'POST':
		query = request.POST.get('search_box')
		# query = request.POST

		if query:
			result_list = handle_query(json_data, query)
			tag_result_list = search_tags(json_data, query)
			text_result_list= search_text(json_data, query)
			# for bk in tag_result_list:
			# 	print bk['pages']
	# print "HERE IS VIEWS QUERY ", query
	context = {
		'query': query,
		'result_list': result_list,
		'tag_result_list': tag_result_list,
		'text_result_list': text_result_list,
	}
	return render(request, 'searchapp/search_results.html', context)

def about(request):
	template = loader.get_template('searchapp/about.html')
	context = {
		'Title': 'About ABCQuery',
	}
	return HttpResponse(template.render(context, request))
