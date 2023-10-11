from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from students.models import Student
from teachers.forms import TeacherForm, GroupForm, StudentGroupForm
from teachers.models import Teacher, Group


def teacher(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teachers/teachers.html", {"form": form})

    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("show_teachers"))


def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teachers/update_teacher.html", {"form": form})

    form = TeacherForm(request.POST, instance=teacher)

    if request.POST.get("delete"):
        teacher.delete()
        return redirect(reverse("show_teachers"))

    if form.is_valid():
        form.save()
        return redirect(reverse("show_teachers"))

    return render(request, "teachers/update_teacher.html", {"form": form})


def show_teachers(request):
    get_teacher_info = Teacher.objects.all()

    data = {
        "data": get_teacher_info,
    }

    return render(request, "teachers/show_teachers.html", data)


def group(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "teachers/groups.html", {"form": form})

    group_form = GroupForm(request.POST)

    if group_form.is_valid():
        curator = group_form.cleaned_data["curator"]
        group_name = group_form.cleaned_data["group_name"]

        Group.objects.create(curator=curator, group_name=group_name)

        return redirect("/groups/")
    else:
        return HttpResponse("Invalid data")


def add_student_in_group(request, pk):
    student1 = get_object_or_404(Student, pk=pk)

    if request.method == "GET":
        form = StudentGroupForm(instance=student1)
        return render(
            request,
            "teachers/add_student_in_group.html",
            {"form": form, "student": student1},
        )

    form = StudentGroupForm(request.POST, instance=student1)
    if form.is_valid():
        form.save()
        form.instance.group.clear()
        form.instance.group.set(form.cleaned_data["group"])
        return redirect(reverse("show_groups"))

    return render(
        request,
        "teachers/add_student_in_group.html",
        {"form": form, "student": student1},
    )


def show_groups(request):
    get_group_info = Group.objects.all()

    data = {"data": get_group_info}
    return render(request, "teachers/show_groups.html", data)
