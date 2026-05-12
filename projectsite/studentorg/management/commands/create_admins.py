from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create two administrator accounts for development and testing.'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        admin_accounts = [
            {
                'username': 'admin1',
                'email': 'admin1@example.com',
                'password': 'Admin@12345',
            },
            {
                'username': 'admin2',
                'email': 'admin2@example.com',
                'password': 'Admin2@12345',
            },
        ]

        for admin in admin_accounts:
            username = admin['username']
            email = admin['email']
            password = admin['password']

            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f"Admin user '{username}' already exists."))
                continue

            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(
                f"Created admin account: username={username}, password={password}, email={email}"
            ))

        self.stdout.write(self.style.SUCCESS('Admin account creation complete.'))
