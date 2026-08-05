from django.contrib.auth.models import User

# Create user with id 1
user, created = User.objects.get_or_create(
    id=1,
    defaults={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'is_staff': False,
        'is_superuser': False
    }
)

if created:
    user.set_password('password123')
    user.save()
    print(f"Created user: {user.username} (id: {user.id})")
else:
    print(f"User already exists: {user.username} (id: {user.id})")
