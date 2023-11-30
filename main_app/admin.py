from django.contrib import admin
from .models import Employee, Skill, Position, Photo

# Register your models here.
admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(Position)
admin.site.register(Photo)