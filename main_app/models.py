from django.db import models
from django.contrib.auth.models import User


# Create your models here.   
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     # Going to try ImageField, but can just make them add an image in 'detail' just like in catcollector
#     # avatar = models.ImageField()
#     admin = models.BooleanField(
#         max_length=1,
#         default=False
#     )

class Skill(models.Model):
    name = models.CharField(max_length=100)
    pay_increase = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    years_employed = models.IntegerField()
    skills = models.ManyToManyField(Skill)
    # availibility = 
    # position = 
    def __str__(self):
        return self.name