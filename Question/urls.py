from django.conf.urls import url

from . import views

app_name = 'Question'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^choices', views.choice.as_view(), name='choice-form'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]