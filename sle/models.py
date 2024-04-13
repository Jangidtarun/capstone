from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
# Create your models here.

# user
class User(AbstractUser):
    batch = models.IntegerField(default=2020)
    admission_type_choices = {
        'regular': 'regular',
        'distance': 'non-regular'
    }
    admission_type = models.CharField(max_length=20, default='regular', choices=admission_type_choices)

    def __str__(self) -> str:
        return self.username



# course
class Course(models.Model):
    course_code = models.CharField(max_length=64)
    title = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=True)
    credit = models.IntegerField(default=1)
    elective_type_choices = {
        'Liberal Arts': 'LA',
        'Departmental Core Theory': 'DCT',
        'Departmental Core Lab': 'DCL',
        'Free Elective': 'FE',
        'Basic Science': 'BS',
        'Basic Engineering Skills': 'BES',
        'Additional': 'Additional',
        'Departmental Elective': 'DE',
        
    }
    elective_type = models.CharField(max_length=60, default='LA', choices=elective_type_choices)
    
    registered_students = models.ManyToManyField(User, blank=True, related_name='ongoing')
    finished_course = models.ManyToManyField(User, blank=True)


    def __str__(self) -> str:
        return self.title


# grade
class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade_point = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username


# 