from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from faker import Faker

from .forms import StudentForm
from .models import Student

fake = Faker()


def student(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "students/student_form.html", {"form": form})

    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("students_list"))

    return render(request, "students/student_form.html", {"form": form})


def update_student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "students/update_students.html", {"form": form})

    form = StudentForm(request.POST, instance=student)

    if request.POST.get("delete"):
        student.delete()
        return redirect(reverse("students_list"))

    if form.is_valid():
        form.save()
        return redirect(reverse("students_list"))

    return render(request, "students/update_students.html", {"form": form})


def students(request):
    data_students = Student.objects.all()
    data = {"data": data_students}
    return render(request, "students/students.html", data)


def generate_one_student(request):
    fake_student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date(),
        year_of_admission=randint(1999, 2024),
    )

    if request.method == "GET":
        get_fake_info = Student.objects.get(pk=fake_student.pk)

        data = {
            "data": get_fake_info,
        }

        return render(request, "students/one_student.html", data)


def generate_students(request):
    count = request.GET.get("count")
    get_fake_info = []

    try:
        if count is None:
            count = 10
        else:
            count = int(count)
    except ValueError:
        return HttpResponse("<h1>Введіть цiле число</h1>")

    if 0 >= count or count > 100:
        return HttpResponse("<h1>Введіть цiле позитивне число не більше 100</h1>")

    for i in range(count):
        fake_student = Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date(),
            year_of_admission=randint(1999, 2024),
        )
        student = Student.objects.get(pk=fake_student.id)
        get_fake_info.append(student)

    data = {
        "data": get_fake_info,
    }

    return render(request, "students/students.html", data)
