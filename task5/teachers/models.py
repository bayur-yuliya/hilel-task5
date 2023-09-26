from django.db import models


class Teacher(models.Model):
    name = models.CharField("name", max_length=20)
    surname = models.CharField("surname", max_length=20)
    birth_date = models.DateField()
    email = models.CharField("subject", max_length=30)

    def __str__(self):
        return str(self.name)
