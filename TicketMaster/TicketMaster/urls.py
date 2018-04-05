from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns = [
	url(r'^new_ticket/$', views.new_ticket, name='new_ticket'),
	url(r'^get_ticket_details/$', views.get_ticket_details, name='get_ticket_details'),
	url(r'^new_update/$', views.new_update, name='new_update'),
	url(r'^get_updates/$', views.get_updates, name='get_updates'),
	url('', views.home, name='home'),
]
