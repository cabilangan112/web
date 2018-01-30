from django import forms

from Faculty.models import detail

from .models import Choice

from django.forms import ModelForm, Textarea

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = [
			'Name_of_Faculty',
		]
		
