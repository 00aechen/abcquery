from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
	url(r'search/$', views.search, name='search'),
	url(r'search_test/$', views.search_test, name='search_test'),
	url(r'results_test/$', views.results_test, name='results_test'),
]