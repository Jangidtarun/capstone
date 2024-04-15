from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Course, Grade, Update

# Create your views here.

def index(req):
    courses = Course.objects.all()
    paginator = Paginator(courses, 20)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    updates = Update.objects.last()
    return render(req, 'sle/index.html', {
        'courses': page_obj,
        'news': updates
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
    updates = Update.objects.last()
    return render(req, 'sle/mycourses.html', {
        'courses': page_obj,
        'news': updates
    })

def filterpage(req):
    if req.method == 'POST':
        status = req.POST['status']


        if status == "both":
            courses = Course.objects.all()
        else:
            courses = Course.objects.filter(
                status = status
            )    
        
        paginator = Paginator(courses, 20)
        page_number = req.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(req, 'sle/index.html', {
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

def feedback(req, course_id):
    course = Course.objects.get(pk=course_id)
    return render(req, 'sle/feedback.html')


def login_view(req):
    if req.method == "POST":

        # Attempt to sign user in
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(req, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(req, "sle/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(req, "sle/login.html")


def logout_view(req):
    logout(req)
    return HttpResponseRedirect(reverse(login_view))


def register(req):
    if req.method == "POST":
        username = req.POST["username"]

        # Ensure password matches confirmation
        password = req.POST["password"]
        confirmation = req.POST["confirmation"]
        if password != confirmation:
            return render(req, "sle/register.html", {
                "message": "Passwords must match."
            })
        
        batch = req.POST['batch']
        adtype = req.POST['adtype']

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username=username, 
                password=password,
                batch=batch,
                admission_type=User.admission_type_choices[adtype]
            )
            user.save()
        except IntegrityError:
            return render(req, "sle/register.html", {
                "message": "Username already taken."
            })
        login(req, user)
        return HttpResponseRedirect(reverse(index))
    else:
        return render(req, "sle/register.html")