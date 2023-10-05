from django.urls import path

from . import views


urlpatterns = [
    path("teacher/", views.teachers, name="teacher"),
    path("teachers/", views.show_teachers, name="show_teachers"),
    path("group/", views.group, name="group"),
    path("groups/", views.show_groups, name="show_groups"),
]
