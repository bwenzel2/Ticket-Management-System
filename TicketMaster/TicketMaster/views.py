from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import Ticket
from TicketMaster.forms import TicketForm


# Create your views here.
def custom_login(request):
	return render(request, 'home.html', {})

def home(request):
	tickets = Ticket.objects.filter()
	if request.user.is_authenticated:
		return render(request, 'home.html', {'tickets': tickets})
	else:
		return redirect('login')
		
def new_ticket(request):
	
	#return redirect('home')
	

	# A HTTP POST?
	if request.method == 'POST':
		desc = request.POST.get('description')
		# only add the new ticket if the description is not empty
		# TO-DO: add validation to prevent this from happening!
		if desc != "":
			# add a new ticket
			t = Ticket.objects.create(description=desc, creator=request.user)
	return redirect('home')
		

