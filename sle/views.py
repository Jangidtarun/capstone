from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Course, Grade

# Create your views here.
def index(req):
    courses = Course.objects.all()
    paginator = Paginator(courses, 20)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req, 'sle/index.html', {
        'courses': page_obj
    })

def mycourses(req):
    courses = Course.objects.all()
    ulist = []
    for course in courses:
        if req.user in course.registered_students.all():
            ulist.append(course)
    paginator = Paginator(ulist, 20)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req, 'sle/mycourses.html', {
        'courses': page_obj
    })

def enroll(req, course_id):
    course = Course.objects.get(pk=course_id)
    course.registered_students.add(req.user)
    return HttpResponseRedirect(reverse(index))

def unenroll(req, course_id):
    course = Course.objects.get(pk=course_id)
    course.registered_students.remove(req.user)
    return HttpResponseRedirect(reverse(mycourses))