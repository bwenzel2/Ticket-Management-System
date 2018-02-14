from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect


# Create your views here.
def custom_login(request):
	return render(request, 'home.html', {})

def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
	else:
		return redirect('login');

