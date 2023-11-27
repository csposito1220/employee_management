from django.db import models

# Create your models here.   
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    # Going to try ImageField, but can just make them add an image in 'detail' just like in catcollector
    # avatar = models.ImageField()
    admin = models.BooleanField(
        max_length=1,
        default=False
    )

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    years_employed = models.IntegerField()
    # skills = models.ManyToManyField(Skill)
    # availibility = 
    # position = 

class Skill(models.Model):
    name = models.CharField(max_length=100)
    date= models.DateField()

    def __str__(self):
        return self.name