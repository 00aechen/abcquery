from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from handle_query import handle_query

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


# def search_test(request):
# 	global query_var
# 	print "search_test was called"
# 	query = request.GET.get('q', '')
# 	t = loader.get_template('searchapp/search_test.html')
# 	context={ 'query': query,}
# 	print "This is the context: ", context
# 	query_var = query
# 	print "q: ", query_var
# 	return HttpResponse(t.render(context, request))

# def results_test(request):
# 	global query_var
# 	print "results_test was called"
# 	t = loader.get_template('searchapp/results_test.html')
# 	query = query_var
# 	print "query: ", query
# 	context={'query':query,}
# 	print "This is the context: ", context 
# 	return HttpResponse(t.render(context, request))
	
def search(request):
	result_list = []

	if request.method == 'POST':
		query = request.POST.get('search_box')
		# query = request.POST

		if query:
			result_list = handle_query(query)
	# print "HERE IS VIEWS QUERY ", query
	context = {
		'query': query,
		'result_list': result_list
	}
	return render(request, 'searchapp/search_results.html', context)

def about(request):
	template = loader.get_template('searchapp/about.html')
	context = {
		'Title': 'About ABCQuery',
	}
	return HttpResponse(template.render(context, request))
