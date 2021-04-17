from django.db import models
from django.db.models.signal import post_save

from django.contrib.auth.models import User
from post.models import Follow
# Create your models here.

def user_directory_path(instance, filename):
	# Returns the filename and path of the post of the user to be uploaded to MEDIA_ROOT
	return "user_{0}/{1}".format(instance.user.id, filename)



class Story(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_user')
	content = models.FileField(upload_to=user_directory_path)
	caption = models.TextField(max_length=50)
	expired = models.BooleanField(default=False)
	posted = models.DateTimeField(auto_add_now=True)

	def __str__(self):
		return self.user.username

class StoryStream(models.Model):
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_following')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	story = models.ManyToManyField(Story, related_name='stories')
	date = models.DateTimeField(auto_add_now=True)

	def __str__(self):
		return self.following.username + ' - ' + str(self.date)

	def add_post(sender, isntance, *args, **kwargs):
		new_story = instance
		user = new_story.user
		followers = Follow.objects.all().filter(following=user)

		