from django.shortcuts import render

from teachers.models import Teacher


def show_teachers(request):
    get_teacher_info = Teacher.objects.all()

    data = {"data": get_teacher_info}
    return render(request, "teachers/teachers.html", data)







