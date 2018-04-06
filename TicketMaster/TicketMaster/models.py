from django.db import models
from django.utils import timezone
import uuid
import time
from django.db import transaction

# Ticket class
class Ticket(models.Model):
	STATUS_CHOICES = (
		(0,'Open'),
		(1,'In Progress'),
		(2,'Closed'),
	)
	
	URGENCY_CHOICES = (
		('High','High'),
		('Medium','Medium'),
		('Low','Low'),
	)

	location = models.CharField(max_length=200, default='')
	creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=1)
	creation_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(default="")
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	requestor = models.CharField(max_length=200, default='')
	urgency = models.CharField(max_length=6)
	
	def create(self):
		self.save()


# Update class		
class Update(models.Model):
	description = models.TextField(default="this is the default description for an update", null=True)
	creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=1)
	creation_date = models.DateTimeField(default=timezone.now)
	ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT, null=True)
	
		
	
