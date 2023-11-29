from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('admin', views.admin, name='admin'),
    path('employees/', views.employees_index, name='index'),
    path("employees/<int:employee_id>/", views.employees_details, name="detail"),
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/create/', views.SkillCreate.as_view(), name='skill_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),
    path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
    path('employees/<int:employee_id>/assoc_skill/', views.assoc_skill, name='assoc_skill'),
    path('employees/<int:employee_id>/unassoc_skill/<int:skill_id>/', views.unassoc_skill, name='unassoc_skill'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employees_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employees_delete'),
]