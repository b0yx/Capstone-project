from rest_framework import serializers
from .models import Menu , Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        meta = Menu
        fields = '__all__'
        