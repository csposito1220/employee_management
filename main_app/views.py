from django.shortcuts import render
from django.views.generic import ListView, CreateView
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

class SkillList(ListView):
    model = Skill
    template_name = 'main_app/skill_list.html'

class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    template_name = 'main_app/skill_form.html'

