# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class detail(models.Model):
	Last_name    		= models.CharField(max_length=200)
	First_name			= models.CharField(max_length=200)
		
	Gender = (
        ('m', 'Male'),
        ('o', 'Female'),
	)
	Sex			 		 =   models.CharField(max_length=1, choices=Gender, blank=True, default='m')
	Faculty_dep			 = models.ForeignKey('Department', on_delete=models.CASCADE)
	def __str__(self):
		return self.Last_name
		
class Department(models.Model):
	dep = (
        ('C', 'CITE'),
	)
	Department			  = models.CharField(max_length=1, choices=dep, blank=True, default='C')
	BSCS				  = models.BooleanField(default=False)
	BSIT				  = models.BooleanField(default=False)
	BSIS				  = models.BooleanField(default=False)
	BSCPE			      = models.BooleanField(default=False)

	
	def __str__(self):
		return self.Department
