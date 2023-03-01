from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    note = models.CharField(max_length=500)
    guest_number = models.IntegerField()

    def __str__(self) -> str:
        return self.last_name
    
class Item(models.Model):
    name = models.CharField(max_length= 100)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name