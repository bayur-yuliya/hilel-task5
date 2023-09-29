from django.urls import path

from . import views


urlpatterns = [path("", views.show_teachers, name="show_teachers")]
