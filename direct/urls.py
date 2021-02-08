from django.urls import path
from direct.views import inbox

urlpatterns = [
	path('', inbox, name='inbox'),
]