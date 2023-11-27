from django.shortcuts import render
from django.views.generic import ListView
from .models import Skill
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
class SkillList(ListView):
    model = Skill
    template_name = 'main_app/skill-list.html'