from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Student

fake = Faker()


def generate_one_student(request):
    fake_student = Student.objects.create(
        first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date()
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
        )
        student = Student.objects.get(pk=fake_student.id)
        get_fake_info.append(student)

    data = {
        "data": get_fake_info,
    }

    return render(request, "students/students.html", data)
