from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    monday_start = models.TimeField(blank=True, null=True, default='00:00')
    monday_end = models.TimeField(blank=True, null=True,  default='00:00')
    tuesday_start = models.TimeField(blank=True, null=True,  default='00:00')
    tuesday_end = models.TimeField(blank=True, null=True,  default='00:00')
    wednesday_start = models.TimeField(blank=True, null=True,  default='00:00')
    wednesday_end = models.TimeField(blank=True, null=True,  default='00:00')
    thursday_start = models.TimeField(blank=True, null=True,  default='00:00')
    thursday_end = models.TimeField(blank=True, null=True,  default='00:00')
    friday_start = models.TimeField(blank=True, null=True,  default='00:00')
    friday_end = models.TimeField(blank=True, null=True,  default='00:00')
    # position = 
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'employee_id': self.id})