from django.urls import path
from stories.views import NewStory, ShowMedia

urlpatterns = [
	path('newstory/', NewStory, 'newstory'),
	path('showmedia/<stream_id>', ShowMedia, 'showmedia')
]