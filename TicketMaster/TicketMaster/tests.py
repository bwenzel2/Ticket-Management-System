import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Ticket
from .models import Update


class TickeModelTests(TestCase):

        @classmethod
        def setUpTestData(cls):
	        #Set up non-modified objects used by all test methods
                desc = "This is a sample description"
                Ticket.objects.create(description=desc, urgency=2, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location")

        def testTicketDescription(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.description, "This is a sample description")

        def testTicketUrgency(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.urgency, "2")

        def testTicketRequestor(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.requestor, "Sample Requestor")

        def testTicketRecipient(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.recipient, "Sample Recipient")


class UpdateLogTests(TestCase) :
        def setUp(self):
                desc1 = "This is a sample description"
                Ticket.objects.create(description=desc1, urgency=2, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location")


        # Testing if the update log is functioning properly with its respective ticket and displayed first
        def testUpdates(self):
                ticket1 = Ticket.objects.get(id=1)
                desc2 = "Testing Description!!"
                ticket2 = Ticket.objects.create(description=desc2, urgency=3, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location")
                new_update = Update.objects.create(description=ticket1.description, ticket=ticket1).id
                all_updates = Update.objects.filter(id=new_update)
                self.assertEqual(ticket1, all_updates[0].ticket)
                self.assertNotEqual(ticket2, all_updates[0].ticket)


        # Storage of multiple updates on one ticket
        def testUpdateStorage(self):
                new_ticket = Ticket.objects.get(id=1)
                desc1 = "Wow this computer is in serious trouble, I have no idea how to solve this. I'll ask my colleagues."
                desc2 = "Identified the virus, working on developing a solution"
                desc3 = "Requires a new computer part. Part has been ordered and will arrive Wednesday."
                desc4 = "Installed part, computer is working, Setting this ticket as resolved."
                update1 = Update.objects.create(description=desc1, ticket=new_ticket)
                update2 = Update.objects.create(description=desc2, ticket=new_ticket)
                update3 = Update.objects.create(description=desc3, ticket=new_ticket)
                update4 = Update.objects.create(description=desc4, ticket=new_ticket)
                updates = [update1, update2, update3, update4]
                all_updates = Update.objects.filter(ticket=new_ticket)
                for i in range(0, 4) :
                        self.assertEqual(all_updates[i].description, updates[i].description)

                        
class TestingStatus(TestCase) :
        def setUp(self):
                Ticket.objects.create(description="This is a test", urgency=1, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location")
        
        #testing if the status is working properly
        def testTicketDescription(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.description, "This is a test")

        def testTicketStatus(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.status,0)
                
class TestingStatus2(TestCase) :
    
        #testing solution and in progress status
        def setUp(self):
                Ticket.objects.create(description="This is a test", urgency=1, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location", status=1, solution="UPdated the server")
                
        def testTicketStatus(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.status,1)
                
        def testTicketStatus(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.solution,"UPdated the server")

class TestingStatus3(TestCase) :
        def setUp(self):
                Ticket.objects.create(description="This is a test", urgency=1, requestor="Sample Requestor", recipient="Sample Recipient", location="Sample Location", status=2, solution="UPdated the server")
                
        #testing closed status
        def testTicketStatus(self):
                new_ticket = Ticket.objects.get(id=1)
                self.assertEqual(new_ticket.status,2)
                
                

            
                
                

                
        
