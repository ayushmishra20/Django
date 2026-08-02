#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Project.settings')
django.setup()

from django.test import Client

c = Client()
resp = c.get('/admin/login/')
print(f'Status: {resp.status_code}')
if resp.status_code == 200:
    print('SUCCESS: Admin login page renders!')
else:
    print(f'ERROR: Status {resp.status_code}')
