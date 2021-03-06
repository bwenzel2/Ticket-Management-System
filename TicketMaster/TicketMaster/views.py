from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import Ticket, Update
from django.core import serializers
from django.http import HttpResponse, Http404

from django.utils import timezone

from django.contrib.auth.decorators import login_required


# Create your views here.
def custom_login(request):
	return render(request, 'home.html', {})

@login_required
def home(request):
	tickets = Ticket.objects.filter()
	return render(request, 'homepage.html', {'tickets': tickets})

#creates a new ticket	
@login_required	
def new_ticket(request):
	if request.method == 'POST':
		desc = request.POST.get('description')
		urgency_level = request.POST.get('urgency')
		requestor = request.POST.get('requestor')
		recipient = request.POST.get('recipient')
		location = request.POST.get('location')
		# only add the new ticket if the description is not empty
		# TO-DO: add validation to prevent this from happening!
		if desc != "":
			# add a new ticket
			t = Ticket.objects.create(description=desc, creator=request.user, urgency=urgency_level, requestor=requestor, recipient=recipient, location=location)
	return redirect('home')


#input: a ticket id
#output: a JSON Object representing all the details of the ticket with the specified id
@login_required
def get_ticket_details(request):
	ticket_id = request.GET.get('ticket_id')
	
	#find the ticket with that id, return it as a response
	ticket = Ticket.objects.filter(id=ticket_id)
	response = serializers.serialize("json", ticket, use_natural_foreign_keys=True)
	return HttpResponse(response, content_type='application/json')

		
#creates a new update for a specified ticket id	
@login_required
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
		response = serializers.serialize("json", update, use_natural_foreign_keys=True)
		return HttpResponse(response, content_type='application/json')
	else:
		raise Http404()
	
#get all updates associcated with a particular ticket id, sorted most recent to least recent, return as a JSON Object
@login_required
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
		
#used to assign tickets to the currently-logged-in user
@login_required
def assign_ticket(request):
	ticket_id = request.POST.get('ticket_id')
	#get the ticket with the id specified in the POST request
	ticket = Ticket.objects.get(id=ticket_id)
	ticket.assigned_user = request.user
	ticket.status = 1
	ticket.save()	#any time you modify a database element in a view, you need to call save() to save the modifications to the database
	
	tickets = Ticket.objects.filter(id=ticket_id)
	response = serializers.serialize("json", tickets, use_natural_foreign_keys=True)
	return HttpResponse(response, content_type='application/json')
	
@login_required
def close_ticket(request):
	ticket_id = request.POST.get('ticket_id')
	solution_text = request.POST.get('solution')
	#get the ticket with the id specified in the POST request
	ticket = Ticket.objects.get(id=ticket_id)
	ticket.assigned_user = request.user
	ticket.status = 2
	ticket.solution = solution_text
	ticket.save()	#any time you modify a database element in a view, you need to call save() to save the modifications to the database
	
	tickets = Ticket.objects.filter(id=ticket_id)
	response = serializers.serialize("json", tickets, use_natural_foreign_keys=True)
	return HttpResponse(response, content_type='application/json')

def about(request):
    return render (request, 'about.html')

def help(request):
    return render (request, 'help.html')

def contact_us(request):
    return render (request, 'contact_us.html')
