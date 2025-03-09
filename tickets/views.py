import requests
from django.db import transaction
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TicketSerializer

@api_view(['GET'])
def home(request):
    return Response("Welcome to the home page!", status=200)

@api_view(['POST'])
def ticket_create(request):
    # Start a transaction
    with transaction.atomic():
        # Validate and save the ticket
        serializer = TicketSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the ticket to the database
            ticket = serializer.save()

            # Prepare the data to be sent to Zapier
            zapier_url = settings.ZAPIER_URL
            zapier_data = {
                "name": ticket.name,
                "description": ticket.description,
                "client_name": ticket.client_name,
                "client_email": ticket.client_email
            }

            # Send data to Zapier (external API)
            response = requests.post(zapier_url, json=zapier_data)

            if response.status_code != 200:
                # If the Zapier call fails, raise an exception to trigger a rollback
                raise Exception("Failed to notify Zapier, rolling back transaction.")

            # Return a success message if everything was successful
            return Response({"message": "Ticket created successfully and data sent to Zapier!"}, status=201)

        else:
            # If the serializer is invalid, no need to call Zapier, just return errors
            return Response({"message": serializer.errors}, status=400)
