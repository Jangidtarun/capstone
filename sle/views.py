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

def feedback(req, course_id):
    course = Course.objects.get(pk=course_id)
    return render(req, 'sle/feedback.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "sle/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "sle/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sle/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "sle/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "sle/register.html")