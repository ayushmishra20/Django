#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Project.settings')
django.setup()

from django.test import Client

c = Client()
resp = c.get('/logout/')
print(f'Status: {resp.status_code}')
content = resp.content.decode()
has_message = 'You have been logged out' in content
print(f'Has logout message: {has_message}')
if resp.status_code == 200:
    print('SUCCESS: Logout page renders correctly!')
else:
    print(f'ERROR: Status {resp.status_code}')
    print(content[:300])
