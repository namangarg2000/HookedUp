from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
	class Meta:
		model= Project
		fields =['title','categories','image','email','description','completed']

		widget = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'email' : forms.TextInput(attrs={'class': 'form-control'}),
			'categories' : forms.Select(attrs={'class': 'form-control'}),
			'description' : forms.Textarea(attrs={'class': 'form-control'}),
		}