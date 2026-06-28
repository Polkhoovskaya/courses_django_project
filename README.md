# courses_django_project

A Django-based web application for managing and viewing online courses. The project provides both a web interface and a REST API for working with courses.

## Features

- View the list of available courses through the web interface.
- Display detailed information about each course.
- REST API for managing courses.
- Create new courses via API.
- Delete existing courses via API.
- Django Admin panel for administration.
- REST API built with Django Tastypie.

## Technologies

- Python
- Django
- Django Tastypie
- SQLite (default)
- Pipenv

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

Run database migrations:

```bash
python manage.py migrate
```

Create a superuser (optional):

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

## Open the application

Web interface:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

## Default Admin Credentials

Username:

```
admin
```

Password:

```
12345
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/v1/courses/` | List all courses |
| GET | `/api/v1/courses/<id>/` | Retrieve course details |
| POST | `/api/v1/courses/` | Create a new course |
| DELETE | `/api/v1/courses/<id>/` | Delete a course |

## Example POST Request

```json
{
    "title": "Complete C# Guide",
    "price": 555,
    "students_qty": 120,
    "reviews_qty": 100,
    "category_id": 1
}
```


This project was created as a learning project to practice Django development, Django Tastypie, and REST API design.
