from django.db import models

# restaurant/models.py
class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} - {self.booking_date}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Adjusted max_digits to allow higher prices
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - {self.price}"
