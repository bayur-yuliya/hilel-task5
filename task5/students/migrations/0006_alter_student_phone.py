# Generated by Django 4.2.5 on 2023-10-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0005_student_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=20, null=True, verbose_name="phone"),
        ),
    ]
