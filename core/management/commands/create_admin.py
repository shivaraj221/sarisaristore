from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = "Create superuser from environment variables"

    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")
        email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        
        if not username or not password:
            self.stdout.write(self.style.ERROR("❌ ADMIN_USERNAME and ADMIN_PASSWORD not set in environment"))
            return
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"⚠️ User '{username}' already exists"))
            return
        
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' created successfully"))
