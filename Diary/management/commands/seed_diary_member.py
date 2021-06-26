from faker import Faker
from django_seed import Seed
from django.core.management.base import BaseCommand
from Accounts.models import User
from Diary.models import Diary
from Diary.models import DiaryMember


class Command(BaseCommand):
    print("hello make diary_member_seed")

    help = "This command create many notification"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=5,
            type=int,
            help="다이어리 멤버 몇개 ??"
        )

    def handle(self, *args, **options):
        number = options.get("number", 5)
        users = User.objects.all()
        fake = Faker(["ko_KR"])

        for diary in Diary.objects.all():
            for user in users:
                if diary.user == user or diary.now_writer == user:
                    continue
                data = dict(
                    nickname=fake.unique.bs(),
                    diary=diary,
                    user=user,
                    profile_img=Seed.seeder().faker.image_url(),
                )
            DiaryMember.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f"{number} created!!!"))
