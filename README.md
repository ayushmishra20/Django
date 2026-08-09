# Django Blog

A simple Django blog project with user registration, login, logout, profiles, and an about page.

## Features

- Blog home page with sample posts
- About page
- User registration with username, email, and password
- Login and logout
- Authenticated user profile page
- Profile image support through the `Profile` model
- Django admin interface
- SQLite database for local development

## Project Structure

```text
Django/
├── README.md
└── Django_Project/
	├── manage.py
	├── db.sqlite3
	├── blog/
	│   ├── models.py
	│   ├── urls.py
	│   ├── views.py
	│   ├── templates/blog/
	│   └── static/Blog/
	├── users/
	│   ├── forms.py
	│   ├── models.py
	│   ├── signals.py
	│   ├── views.py
	│   └── templates/users/
	├── Django_Project/
	│   ├── settings.py
	│   └── urls.py
	└── media/profile_pics/
```

## Requirements

- Python 3
- Django
- django-crispy-forms
- crispy-bootstrap4
- Pillow

## Installation

From the repository root, open a terminal and run:

```bash
python -m pip install Django django-crispy-forms crispy-bootstrap4 Pillow
```

Apply migrations:

```bash
python manage.py migrate
```

Optionally create an administrator account:

```bash
python manage.py createsuperuser
```

## Run the Project

Start the development server from the `Django_Project` directory:

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## Routes

| URL          | Description                       |
| ------------ | --------------------------------- |
| `/`          | Blog home page                    |
| `/about/`    | About page                        |
| `/register/` | Create a user account             |
| `/login/`    | Sign in                           |
| `/logout/`   | Sign out                          |
| `/profile/`  | View the signed-in user's profile |
| `/admin/`    | Django administration             |

## Development Notes

- The project uses SQLite and stores the database in `Django_Project/db.sqlite3`.
- Uploaded profile images are stored under `Django_Project/media/profile_pics/`.
- `blog/views.py` currently displays sample posts from an in-memory list. The `blog.models.Post` model is available for database-backed posts.
- `DEBUG` is enabled for local development. Set a secure `SECRET_KEY`, configure `ALLOWED_HOSTS`, and disable debug mode before deploying.

## Run Tests

Run the test suite with:

```bash
python manage.py test
```
