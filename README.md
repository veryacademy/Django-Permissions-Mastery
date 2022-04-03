# Documentation

## Tutorial Content Overview

---

Presentation:

    - [ ] Authentication vs Permissions (Authorisation)
    - [ ] Identity and access management - Authentication
    - [ ] Identity and access management - Authorisation
    - [ ] User Object

Code:

    - [ ] Create new project
    - [ ] Migrate
    - [ ] Create 3 user types
    - [ ] Default user access to admin
 
Presentation:

    - [ ] Common Authorisation Methods
    - [ ] Permissions (Authentication)
    - [ ] django.contrib.auth

Code:

    - [ ] Inspect permission models
    - [ ] Permission ERD

    - [ ] Remove admin permissions from User and Group Model
    - [ ] Setup a Custom User Admin and assign to models
    - [ ] Add permissions to Staff to edit users
    - [ ] Disable fields

    - [ ] Create new model (Inventory)
    - [ ] Permission naming convention
    - [ ] Add permissions to Staff to edit users
    - [ ] Disable selected fields
    
Presentation:

    - [ ] Group permissions

Code:

    - [ ] Create group - apply permissions
    - [ ] Add group to user

    - [ ] Override Permission
    - [ ] remove the ‘Add’/’Delete’ button for a model




user@host> manage.py shell
from django.contrib.auth.models import User
u=User.objects.create_user('user', password='user')
u.is_superuser=True
u.is_staff=True
u.save()

from django.contrib.auth.models import User
u=User.objects.create_user('admin', password='admin')
user=User.objects.create_user('user', password='user')
user.save()

u=User.objects.create_user('staff', password='staff')
u.is_superuser=True
u.is_staff=True
user.save()

from django.contrib.auth.models import User
u = User.objects.get(username='staff')
u.has_perm('auth.change_user')
False


References:
https://realpython.com/manage-users-in-django-admin/#model-permissions