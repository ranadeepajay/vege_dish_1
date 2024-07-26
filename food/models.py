from django.db import models

# Create your models here.



class Dish(models.Model):
    dish_name=models.CharField(max_length=100)
    dish_description=models.TextField()
    dish_image=models.ImageField()