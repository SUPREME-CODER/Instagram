from django.contrib import admin
from stories.models import Story, StoryStream

# Register your models here.
admin.site.Register(Story)
admin.site.Register(StoryStream)