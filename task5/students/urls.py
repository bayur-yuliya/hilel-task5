from django.urls import path

from . import views

urlpatterns = [
    path("student/", views.student, name="student"),
    path("students_list/", views.students, name="students_list"),
    path("update-student/<int:pk>/", views.update_student, name="update_student"),
    path("generate-student/", views.generate_one_student, name="generate_one_student"),
    path("generate-students/", views.generate_students, name="generate_students"),
]
