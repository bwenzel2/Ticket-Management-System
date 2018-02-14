from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
	url('', views.home, name='home'),
]
