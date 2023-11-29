import os
from django import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
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
    id_list = employee.skills.all().values_list('id')
    skills_employee_doesnt_have = Skill.objects.exclude(id__in=id_list)
    return render(request, 'employees/detail.html', { 'employee': employee,
    'skills': skills_employee_doesnt_have,                                              
    })
    

    
class EmployeeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
   model = Employee
   fields = '__all__'
   success_url = '/employees'

   def test_func(self):
        # The user passes the test if they are a superuser
        return self.request.user.is_superuser



class SkillList(ListView):
    model = Skill
    template_name = 'main_app/skill_list.html'

class SkillCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Skill
    fields = '__all__'
    template_name = 'main_app/skill_form.html'
    success_url = '/skills'

    def test_func(self):
        # The user passes the test if they are a superuser
        return self.request.user.is_superuser



class SkillDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Skill
   success_url = '/skills'

   def test_func(self):
        # The user passes the test if they are a superuser
        return self.request.user.is_superuser



class SkillUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Skill
   fields = ['name', 'pay_increase']
   success_url = '/skills'

   def test_func(self):
        # The user passes the test if they are a superuser
        return self.request.user.is_superuser


class SignupForm(UserCreationForm):
   is_superuser = forms.BooleanField(required=False)
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2', 'is_superuser']
    

    
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

def assoc_skill(request, employee_id):
    if request.method == 'POST':
        skill_id = request.POST.get('skill_id')
        Employee.objects.get(id=employee_id).skills.add(skill_id)
        return redirect('detail', employee_id=employee_id)
def unassoc_skill(request, employee_id, skill_id):
    Employee.objects.get(id=employee_id).skills.remove(skill_id)
    return redirect("detail", employee_id=employee_id)
