#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Project.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import Profile

# Create profiles for all users who don't have one
for user in User.objects.all():
    if not hasattr(user, 'profile') or user.profile is None:
        try:
            Profile.objects.create(user=user)
            print(f"Created profile for user: {user.username}")
        except Exception as e:
            print(f"Error creating profile for {user.username}: {e}")

print("Profile sync complete!")
