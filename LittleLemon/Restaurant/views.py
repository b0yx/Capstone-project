from django.shortcuts import render
from rest_framework.response import Response  # Correct import for DRF responses
import rest_framework
from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView , RetrieveUpdateAPIView
from .models import Menu , Booking # Replace with your actual model
from .Seralizer import UserSerializer , BookingSerializer  # Replace with your actual serializer


# Create your views here.
def index(request):
    return render(request, 'index.html')  # No need to include 'templates/' in the path

class MenuItemView(rest_framework.generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = UserSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = UserSerializer
    
class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer