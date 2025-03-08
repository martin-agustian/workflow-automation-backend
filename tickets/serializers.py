from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    client_email = serializers.EmailField(required=True, allow_blank=False)
    client_name = serializers.CharField(required=True, max_length=255)
    name = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True)
    
    class Meta:
        model = Ticket
        fields = '__all__'
