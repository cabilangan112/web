# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import detail, Department 

  
	

admin.site.register(detail)
admin.site.register(Department)
 