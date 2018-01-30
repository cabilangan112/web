# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.shortcuts import render
from .models import Question, Choice
from django.urls import reverse
from Faculty.models import detail
from .forms import ChoiceForm
from django.views.generic import DetailView,View,ListView


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'detail.html', {'question': question})
	
class choice(View):
	def get(self, request):
		choices = Choice.objects.all()
		context = {
			'choices' :choices,
			'form' : ChoiceForm,
		}
		return render(request, "choiceform.html", context)
	
	def post(self, request):
		
		form = ChoiceForm(request.POST)
		choices = Choice.objects.all()
		
		if form.is_valid():
			form.save()
			return redirect('Choice')
			
		context = {
			'form' : form,
			'choices' : choices,
		}
		
		return render(request, "choiceform.html", context)
	
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})
	
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
		return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
         })
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('Question:results', args=(question.id,)))