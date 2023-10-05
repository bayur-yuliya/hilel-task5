from django.db import models


class Teacher(models.Model):
    name = models.CharField("name", max_length=20)
    middle_name = models.CharField("middle name", max_length=20, null=True, blank=True)
    surname = models.CharField("surname", max_length=20)
    birth_date = models.DateField()
    email = models.EmailField("email", max_length=30)
    subject = models.CharField("subject", max_length=70)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group(models.Model):
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_name = models.CharField("group name", max_length=30)

    def __str__(self):
        return str(self.group_name)
