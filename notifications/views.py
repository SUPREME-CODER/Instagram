from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from notifications.models import Notifications
# Create your views here.

def ShowNotifications(request):
	user = request.user
	notifications = Notifications.objects.filter(user=user).order_by('-date')

	template = loader.get_template('notifications.html')

	context = {
				'notifications':notifications,
	}

	return HttpResponse(template.render(context, request))

def DeleteNotifications(request, noti_id):
	user = request.user
	Notifications.objects.filter(id=noti_id, user=user).delete()
	return redirect('show-notifications')