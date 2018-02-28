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
		
def add_ticket(request):
	# Get the context from the request.
	context = RequestContext(request)

	# A HTTP POST?
	if request.method == 'POST':
		form = TicketForm(request.POST)
		
		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage.
			return index(request)
		else:
			# The supplied form contained errors - just print them to the terminal.
			print(form.errors)
		return render_to_response('home.html', {'form': form}, context)
	else:
		return redirect('login')
		

