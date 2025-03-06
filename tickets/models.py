from django.db import models

class Ticket(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    request = models.TextField()
    status = models.CharField(max_length=100, default="New")

    def __str__(self):
        return f"Ticket {self.id} from {self.client_name}"
