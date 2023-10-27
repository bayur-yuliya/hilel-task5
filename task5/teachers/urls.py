from django.urls import path

from . import views


urlpatterns = [
    path("teacher/", views.teacher, name="teacher"),
    path("update-teacher/<int:pk>", views.update_teacher, name="update_teacher"),
    path("teachers/", views.show_teachers, name="show_teachers"),
    path("group/", views.group, name="group"),
    path("groups/", views.show_groups, name="show_groups"),
    path(
        "add-student-in-group/<int:pk>",
        views.add_student_in_group,
        name="add_student_in_group",
    ),
]
