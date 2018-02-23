from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import Ticket


# Create your views here.
def custom_login(request):
	return render(request, 'home.html', {})

def home(request):
	tickets = Ticket.objects.filter()
	if request.user.is_authenticated:
		return render(request, 'home.html', {'tickets': tickets})
	else:
		return redirect('login');

