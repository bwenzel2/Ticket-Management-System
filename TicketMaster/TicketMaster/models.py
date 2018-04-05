from django.db import models
from django.utils import timezone
import uuid
#from hashids import Hashids
import time
from django.db import transaction

class Ticket(models.Model):
	
	#hashids = Hashids(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
	
	STATUS_CHOICES = (
				(0,'Open'),
				(1,'In Progress'),
				(2,'Closed'),
		  )
	#external_id = models.CharField(max_length=200, default="hippo") #models.UUIDField(default=uuid.uuid4)
	location = models.CharField(max_length=200, default='')
	creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=1)
	creation_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(default="")
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	requestor = models.CharField(max_length=200, default='')
	urgency = models.BooleanField(default=False)
	#update_messages = ArrayField(
	#		models.CharField(max_length=500, default=''),
	#		null=True,
	#	)
	
	
	
	def create(self):
		self.save()
		
class Update(models.Model):
	description = models.TextField(default="this is the default description for an update", null=True)
	creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=1)
	creation_date = models.DateTimeField(default=timezone.now)
	ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT, null=True)
	
		
	
