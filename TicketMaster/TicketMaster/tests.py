import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Ticket


class TickeModelTests(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		#Set up non-modified objects used by all test methods
		desc = "This is a sample description"
		Ticket.objects.create(description=desc, urgency=2, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location")
	
	def testTicketDescription(self):
		new_ticket = Ticket.objects.get(id=1)
		self.assertEqual(new_ticket.description, "This is a sample description")
