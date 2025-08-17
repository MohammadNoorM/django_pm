from django import forms
from . import models


attrs = {'class': 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs),
            'category': forms.Select(attrs=attrs),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'category': forms.Select(attrs=attrs),
            'status': forms.Select(attrs=attrs),
        }
