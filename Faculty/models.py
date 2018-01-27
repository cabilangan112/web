# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from datetime import time
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse


class detail(models.Model):
	Last_name    		 = models.CharField(max_length=200)
	First_name			 = models.CharField(max_length=200)	
	Subject				 = models.CharField(max_length=200)
	Evaluation_Date      = models.DateField(default=date.today)
	Time			     = models.TimeField(null=True, blank=True)
	
	
	def __str__(self):
		return self.Last_name
	
	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])