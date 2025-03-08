from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()

    def __str__(self):
        return f"Ticket {self.id} from {self.client_name}"
