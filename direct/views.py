from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader 

# models
from direct.models import Message

# Create your views here.
@login_required
def inbox(request):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message.objects.filter(user=user, recipient=message['user'])
		directs.update(is_read=True)

		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

		context = {
			'directs': directs,
			'active_direct': active_direct,
			'messages': messages,
		}

	template = loader.get_template('direct.html')

	return HttpResponse(template.render(context, request))

@login_required
def Directs(request, username):
	user = request.user
	messages = Message.objects.filter(user=user)
	active_direct = username
	directs = Message.objects.filter(user=user, recipient_username=username)
	directs.update(is_read = True)

	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'directs' : directs,
		'messages': messages,
		'active_direct':active_direct,
	}

	template = loader.get_template('direct.html')

	return HttpResponse(template.render(context, request))

@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')

	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()