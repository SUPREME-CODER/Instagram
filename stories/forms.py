from django import forms

from stories.models import Story

from django.forms import ClearableFileInput

class NewStoryForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), require=True)
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'input is-medium'}), require=True)

	class Meta:
		model = Story
		fields = ('content', 'caption')