from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mycourses', views.mycourses, name='mycourses'),
    path('enroll/<int:course_id>', views.enroll, name='enroll'),
    path('unenroll/<int:course_id>', views.unenroll, name='unenroll'),
    path('feedback/<int:course_id>', views.feedback, name='feedback'),
]