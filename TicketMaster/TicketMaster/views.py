from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import Ticket, Update
from django.core import serializers
from django.http import HttpResponse, Http404


# Create your views here.
def custom_login(request):
	return render(request, 'home.html', {})

def home(request):
	tickets = Ticket.objects.filter()
	if request.user.is_authenticated:
		return render(request, 'home.html', {'tickets': tickets})
	else:
		return redirect('login')

#creates a new ticket		
def new_ticket(request):
	if request.method == 'POST':
		desc = request.POST.get('description')
		urgency_level = request.POST.get('urgency')
		# only add the new ticket if the description is not empty
		# TO-DO: add validation to prevent this from happening!
		if desc != "":
			# add a new ticket
			t = Ticket.objects.create(description=desc, creator=request.user, urgency=urgency_level)
	return redirect('home')


#input: a ticket id
#output: a JSON Object representing all the details of the ticket with the specified id
def get_ticket_details(request):
	ticket_id = request.GET.get('ticket_id')
	
	#find the ticket with that id, return it as a response
	ticket = Ticket.objects.filter(id=ticket_id)
	response = serializers.serialize("json", ticket)
	return HttpResponse(response, content_type='application/json')

		
#creates a new update for a specified ticket id	
def new_update(request):
	if request.method == 'POST':
		#get the POST paramenters
		desc = request.POST.get('description')
		ticket_id = request.POST.get('ticket_id')
		
		#get the ticket with the id specified in the POST request
		t = Ticket.objects.get(id=ticket_id)
		
		#create a new ticket and store its id
		newId = Update.objects.create(description=desc, ticket=t).id	
		
		#use the id of the new ticket to create a queryset to send back to the client
		update = Update.objects.filter(id=newId)
		response = serializers.serialize("json", update)
		return HttpResponse(response, content_type='application/json')
	else:
		raise Http404()
	
#get all updates associcated with a particular ticket id, sorted most recent to least recent, return as a JSON Object
def get_updates(request):
	if request.method == 'GET':		
		ticket_id = request.GET.get('ticket_id')
		#https://stackoverflow.com/questions/761352/django-queryset-order
		updates = Update.objects.filter(ticket=ticket_id).order_by('-creation_date')
		
		#https://stackoverflow.com/questions/26373992/use-jsonresponse-to-serialize-a-queryset-in-django-1-7
		response = serializers.serialize("json", updates)
		return HttpResponse(response, content_type='application/json')
		
	else:
		return redirect('login')
		

