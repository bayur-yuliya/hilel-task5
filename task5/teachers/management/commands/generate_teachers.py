from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from teachers.models import Teacher


fake = Faker()


class Command(BaseCommand):
    help = """the command generates a list of teachers, 
            if you do not specify a parameter, by default 100 teachers are generated"""

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=100)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            create_teachers = Teacher.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                birth_date=fake.date(),
                email=fake.email(),
            )

            self.stdout.write(
                self.style.SUCCESS(f"Все прошло успешно! ({create_teachers.id})")
            )
