import this
from django.db import models

class Plant(models.Model):
    common_name=models.CharField(max_length=70)
    botanical_name=models.CharField(max_length=100)
    family_name= models.CharField(max_length=70)
    plant_type = models.CharField(max_length=50)
    sun_exposure = models.CharField(max_length=60)
    native_area = models.CharField(max_length=100)
    watering_schedule = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.common_name


class Fern(Plant,models.Model):
    
    def __str__(self) -> str:
        return self.common_name

class Succulent(Plant, models.Model):
    
    def __str__(self) -> str:
        return self.common_name

class Vine(Plant, models.Model):
    
    def __str__(self) -> str:
        return self.common_name


class Shopper(models.Model):
    name = models.CharField(max_length=130)
    id = models.BigAutoField(primary_key=True)
    items = models.ManyToManyField(Plant)

    #TODO:Create function for handling new object when front-end is called.

    
    def __str__(self) -> str:
        return self.name
