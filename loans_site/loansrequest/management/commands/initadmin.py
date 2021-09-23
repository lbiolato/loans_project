from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from loans_site import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).count() == 0:
            username = settings.ADMINS[0][0].replace(' ', '')
            email = settings.ADMINS[0][1]
            password = 'admin'
            User.objects.create_superuser(email=email, username=username, password=password)
    