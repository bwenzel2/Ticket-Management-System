from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import Ticket
from TicketMaster.forms import TicketForm
from django.core import serializers
from django.http import HttpResponse


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
	if request.method == 'POST':
		desc = request.POST.get('description')
		# only add the new ticket if the description is not empty
		# TO-DO: add validation to prevent this from happening!
		if desc != "":
			# add a new ticket
			t = Ticket.objects.create(description=desc, creator=request.user)
	return redirect('home')
	
def get_ticket_details(request):
	ticket_id = request.GET.get('ticket_id')
	
	ticket = Ticket.objects.filter(id=ticket_id)
	response = serializers.serialize("json", ticket)
	return HttpResponse(response, content_type='application/json')
		
	
def new_update(request):
	if request.method == 'POST':
		desc = request.POST.get('description')
		ticket_id = request.POST.get('ticket_id')
		update = Update.objects.create(description=desc, ticket = Ticket.objects.get(pk=ticket_id))		
	return redirect('home')
	
def get_updates(request):
	if request.method == 'GET':
		updates = Ticket.objects.all()
		
		#https://stackoverflow.com/questions/26373992/use-jsonresponse-to-serialize-a-queryset-in-django-1-7
		response = serializers.serialize("json", updates)
		return HttpResponse(response, content_type='application/json')
		
	else:
		return redirect('login')
		

