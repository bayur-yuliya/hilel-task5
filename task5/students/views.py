from faker import Faker

from django.shortcuts import render

from .models import Student

fake = Faker()


def student_info_generate():
    return Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date())


def generate_one_student(request):
    fake_student = student_info_generate()
    get_fake_info = Student.objects.get(pk=fake_student.pk)

    data = {
        'data': get_fake_info,
    }

    return render(request, 'students/one_student.html', data)


def generate_students(request):
    count = request.GET.get('count')
    get_fake_info = []

    for i in range(int(count)):
        fake_student = student_info_generate()
        student = Student.objects.get(pk=fake_student.id)
        get_fake_info.append(student)

    data = {
        'data': get_fake_info,
    }

    return render(request, 'students/students.html', data)
