from django.db import models
from django.utils import timezone

class Ticket(models.Model):
	room = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	
