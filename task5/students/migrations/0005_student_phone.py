# Generated by Django 4.2.5 on 2023-10-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0004_student_group_alter_student_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=12, null=True, verbose_name="phone"),
        ),
    ]
