import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skill, Employee
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def employees_index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {
        'employees': employees
    })
def employees_details(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employees/detail.html', { 'employee': employee})

class EmployeeCreate(LoginRequiredMixin, CreateView):
   model = Employee
   fields = '__all__'
   success_url = '/employees'



class SkillList(ListView):
    model = Skill
    template_name = 'main_app/skill_list.html'

class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    template_name = 'main_app/skill_form.html'
    success_url = '/skills'


    
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)