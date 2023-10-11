# Generated by Django 4.2.5 on 2023-10-09 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_student_year_of_admission"),
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group_name",
                    models.CharField(max_length=30, verbose_name="group name"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="teacher",
            name="middle_name",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="middle name"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="subject",
            field=models.CharField(max_length=70, verbose_name="subject"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="teacher",
            name="email",
            field=models.EmailField(max_length=30, verbose_name="email"),
        ),
        migrations.CreateModel(
            name="TeacherGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="teachers.group"
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="students.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="curator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="teachers.teacher"
            ),
        ),
    ]
