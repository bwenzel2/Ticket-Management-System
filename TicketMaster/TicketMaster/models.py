from django.db import models
from django.utils import timezone

class Ticket(models.Model):
	OPEN = 'OPEN'
	IN_PROGRESS = 'IN PROGRESS'
	CLOSED = 'CLOSED'
	STATUS_CHOICES = (
		(OPEN, 'Open'),
		(IN_PROGRESS, 'In Progress'),
		(CLOSED, 'Closed'),
	)
	room = models.CharField(max_length=200, default='')
	#created_date = models.DateTimeField(default=timezone.now)
	#description = models.TextField(default='')
	#status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=OPEN)
	
	def create(self):
		#creation_date = timezone.now()
		#status = Ticket.objects.filter(status=Ticket.OPEN)
		self.save();
	
