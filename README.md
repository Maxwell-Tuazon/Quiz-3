# Django Job Board

A simple Django-based job board application.

## Features
- User authentication
- Job listing, creation, update, and deletion
- Job application system

## Setup

1. Clone the repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run migrations:  
   `python manage.py migrate`
4. Create a superuser:  
   `python manage.py createsuperuser`
   Follow the prompts to set up the admin user.
5. Start the server:  
   `python manage.py runserver`
6. . If superuser does not have admin privileges, you can manually add them in the Django admin interface.
    or use the shell:
     python manage.py shell
     from accounts.models import CustomUser
     user = CustomUser.objects.get(username='UsernameofyourSuperUser')
     user.is_staff = True
     user.is_superuser = True
     user.save()