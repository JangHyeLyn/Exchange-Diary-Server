from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from Accounts.models import User

class Command(BaseCommand):
    print("hello make user_seed")

    help = "This command create many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want me to create you"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} created!!!"))