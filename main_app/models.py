from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    # Going to try ImageField, but can just make them add an image in 'detail' just like in catcollector
    avatar = models.ImageField()
    admin = models.BooleanField(
        max_length=1,
        default=False
    )
    
