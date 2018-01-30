# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from Faculty.models import detail

class Question(models.Model):

	question_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	

	def __str__(self):
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
		
class Choice(models.Model):
	Name_of_Faculty = models.ForeignKey(detail, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	comment = models.TextField()
	
	def __str__(self):
		return self.choice_text