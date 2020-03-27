# forms.py 
from django import forms 
from .models import *

class uploadForm(forms.ModelForm): 

	class Meta: 
		model = upload 
		fields = ('image')
