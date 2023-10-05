from django.http import HttpResponse
from django.shortcuts import render, redirect

from teachers.forms import TeacherForm, GroupForm
from teachers.models import Teacher, Group


def teachers(request):
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)

        if teacher_form.is_valid():
            name = teacher_form.cleaned_data["name"]
            middle_name = "Null"
            surname = teacher_form.cleaned_data["surname"]
            birth_date = teacher_form.cleaned_data["birth_date"]
            email = teacher_form.cleaned_data["email"]
            subject = teacher_form.cleaned_data["subject"]

            if teacher_form.cleaned_data["middle_name"]:
                middle_name = teacher_form.cleaned_data["middle_name"]

            Teacher.objects.create(
                name=name,
                surname=surname,
                middle_name=middle_name,
                birth_date=birth_date,
                email=email,
                subject=subject,
            )

            return redirect("/teachers/")
        else:
            return HttpResponse("Invalid data")

    teacher_form = TeacherForm()

    form = {
        "form": teacher_form,
    }
    return render(request, "teachers/teachers.html", form)


def show_teachers(request):
    get_teacher_info = Teacher.objects.all()

    data = {
        "data": get_teacher_info,
    }

    return render(request, "teachers/show_teachers.html", data)


def group(request):
    if request.method == "POST":
        group_form = GroupForm(request.POST)

        if group_form.is_valid():
            curator = group_form.cleaned_data["curator"]
            group_name = group_form.cleaned_data["group_name"]

            Group.objects.create(curator=curator, group_name=group_name)

            return redirect("/groups/")
        else:
            return HttpResponse("Invalid data")

    group_form = GroupForm()
    form = {"form": group_form}

    return render(request, "teachers/groups.html", form)


def show_groups(request):
    get_group_info = Group.objects.all()

    data = {"data": get_group_info}
    return render(request, "teachers/show_groups.html", data)
