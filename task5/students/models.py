from django.db import models

from teachers.models import Group


class Student(models.Model):
    first_name = models.CharField("first name", max_length=30)
    last_name = models.CharField("last name", max_length=30)
    birth_date = models.DateField()
    year_of_admission = models.PositiveIntegerField("year of admission")
    phone = models.CharField("phone", max_length=20, null=True)
    group = models.ManyToManyField(Group, related_name="student")

    def __str__(self):
        return f"{str(self.first_name)} {str(self.last_name)}"
