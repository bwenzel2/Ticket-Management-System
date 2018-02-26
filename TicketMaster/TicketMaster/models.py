from django.db import models
from django.utils import timezone

class Ticket(models.Model):
	
	STATUS_CHOICES = (
				(0,'Open'),
				(1,'In Progress'),
				(2,'Closed'),
		  )
	
	room = models.CharField(max_length=200, default='')
	created_date = models.DateTimeField(default=timezone.now)
	#description = models.TextField(default="This is the default description")
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	
	def create(self):
		creation_date = timezone.now()
		#status = Ticket.objects.filter(status=Ticket.OPEN)
		self.save();
	
