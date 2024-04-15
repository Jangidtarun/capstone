from django.contrib import admin
from .models import User, Course, Grade, Update

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Update)