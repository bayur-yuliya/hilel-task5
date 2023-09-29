from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.generate_one_student, name="one_student"),
    path("generate-students/", views.generate_students, name="students"),
]
