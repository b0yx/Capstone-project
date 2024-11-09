from django.contrib.auth.models import User
from .models import Booking
from rest_framework import serializers
from rest_framework import generics

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # The model this serializer is based on
        fields = '__all__'  # Include all fields from the Booking model
    