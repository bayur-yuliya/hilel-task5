# Generated by Django 4.2.5 on 2023-09-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("name", models.CharField(max_length=20, verbose_name="name")),
                ("surname", models.CharField(max_length=20, verbose_name="surname")),
                ("birth_date", models.DateField()),
                ("email", models.CharField(max_length=30, verbose_name="subject")),
            ],
        ),
    ]
