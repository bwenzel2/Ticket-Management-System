from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
import uuid

class Ticket(models.Model):
	
	STATUS_CHOICES = (
				(0,'Open'),
				(1,'In Progress'),
				(2,'Closed'),
		  )
	#external_id = models.UUIDField(default=uuid.uuid4)
	#room = models.CharField(max_length=200, default='')
	creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=1)
	created_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(default="")
	#status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	#update_messages = ArrayField(
	#		models.CharField(max_length=500, default=''),
	#		null=True,
	#	)
	
	
	def create(self):
		self.save();
	
