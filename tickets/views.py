from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket
from .serializers import TicketSerializer

@api_view(['GET'])
def home(request):
    return Response("Welcome to the home page!", status=200)

@api_view(['POST'])
def ticket_create(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Ticket created successfully!"}, status=201)
    return Response(serializer.errors, status=400)
