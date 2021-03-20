from django.db import models
from django.contrib.auth.models import User

from post.models import Post
# Create your models here.

class Notifications(models.Model):
	NOTIFICATION_TYPES = ((1, 'Like'),(2, 'Comment'), (3, 'Follow'))

