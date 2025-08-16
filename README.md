```markdown
# Django Job Board

A Django-based company portal for posting and applying to job openings.

## Features

- Custom user registration with validation
- Company admin can post job openings (via Django Admin)
- Users can apply for jobs and upload resumes
- Bootstrap-based UI (locally hosted, no custom CSS)
- Search and filter job listings
- Authentication and authorization for job details

## Requirements

- Python 3.8+
- pip
- Django 4.2+

## Setup Instructions

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply migrations

```sh
python manage.py migrate
```

### 5. Collect static files (for Bootstrap)

```sh
python manage.py collectstatic
```

### 6. Run the development server

```sh
python manage.py runserver
```

## Admin Privileges

(After Creating superuser "py manage.py createsuperuser")If your superuser does not have admin privileges, you can manually add them in the Django admin interface, or use the shell:

```sh
python manage.py shell
```

```python
from accounts.models import CustomUser
user = CustomUser.objects.get(username='UsernameofyourSuperUser')
user.is_staff = True
user.is_superuser = True
user.save()
```

## Usage

- Access the site at `http://127.0.0.1:8000/`
- Register a new user or log in as admin to post jobs
- Apply for jobs and upload your resume

## Notes

- Only emails ending with `@objor.com` are allowed for registration  
  `# Example: quiz3@objor.com`
- Example job object: `jobObjor`
- Example queryset: `foo`
```

Replace `<your-repo-url>` and `<your-project-folder>` with your actual repository details.
