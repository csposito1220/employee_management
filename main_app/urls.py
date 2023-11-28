from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('employees/', views.employees_index, name='index'),
    path("employees/<int:employee_id>/", views.employees_details, name="detail"),
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/create/', views.SkillCreate.as_view(), name='skill_create'),
    
    path('accounts/signup/', views.signup, name='signup'),
    path('employees/<int:employee_id>/assoc_skill/', views.assoc_skill, name='assoc_skill'),
    path('employees/<int:employee_id>/unassoc_skill/<int:skill_id>/', views.unassoc_skill, name='unassoc_skill'),
]