from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from stories.models import Story, StoryStream
from stories.form import NewStoryForm

from datetime import datetime, timedelta

# Create your views here.
@login_required
def NewStory(request):
	user = request.user
	file_ojs = []

	if request.method == 'POST':
		form = NewStoryForm(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES.get('content')
			caption = form.cleaned_data.get('caption')

			story = Story(user=user, content=file, caption=caption)
			story.save()
			return redirect('index')
	else:
		form = NewStoryForm()

	context = {
		'form':form
	}

	return render(request, 'newstory.html', context)