"""
Auto-create superuser on deployment
Run with: python manage.py createsu
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create superuser automatically'

    def handle(self, *args, **kwargs):
        # Get credentials from environment or use defaults
        username = os.getenv('ADMIN_USERNAME', 'admin')
        password = os.getenv('ADMIN_PASSWORD', 'Admin@2025!')
        email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
        
        # Check if superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'✅ Superuser "{username}" already exists')
            return
        
        # Create superuser
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        self.stdout.write(f'✅ Superuser "{username}" created successfully!')
        self.stdout.write(f'📋 Username: {username}')
        self.stdout.write(f'🔑 Password: {password}')