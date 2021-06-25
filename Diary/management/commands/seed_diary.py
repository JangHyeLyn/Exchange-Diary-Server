from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from Accounts.models import User
from Diary.models import Diary
from notification.models import Notification

class Command(BaseCommand):
    print("hello make notification_seed")

    help = "This command create many notification"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=20,
            type=int,
            help="각 유저별 알림 몇개 생성?"
        )

    def handle(self, *args, **options):
        number = options.get("number", 20)
        users = User.objects.all()
        fake = Faker(["ko_KR"])

        for user in users:
            data = dict(
                title=fake.unique.bs(),
                now_page=1,
                total_page=30,
                now_writer=user,
                user=user,
                cover=1,
                promise=fake.unique.bs(),
                group=None,
                status=0
            )
            Diary.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f"{number} created!!!"))