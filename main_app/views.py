import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skill, Employee, User
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

class SkillList(ListView):
    model = Skill
    template_name = 'main_app/skill-list.html'

class UserCreate(LoginRequireMixin, CreateView):
    model = User
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)