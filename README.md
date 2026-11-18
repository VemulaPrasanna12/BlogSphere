# B# BlogSphere

BlogSphere is a Django blogging platform where visitors can browse posts and staff can manage blog content through a protected dashboard.

## Features

- Browse posts with pagination (six posts per page)
- View individual posts using unique URL slugs
- Display post images, authors, and publication dates
- Staff sign-in and protected content dashboard
- Create, edit, and delete posts
- Django admin interface

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Django templates

## Installation

1. Clone the repository and enter the project directory:

   ```bash
   git clone <repository-url>
   cd blogsphere
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   **Windows PowerShell**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install django pillow
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a staff account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

Visit <http://127.0.0.1:8000/> to browse the site. Staff can sign in at <http://127.0.0.1:8000/admin-login/>. The Django admin is available at <http://127.0.0.1:8000/admin/>.

## Database Setup

BlogSphere uses SQLite by default. The database is stored in `db.sqlite3` in the project root.

After changing the models, create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Routes

These are Django web routes; the project does not currently provide a REST API.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Browse paginated posts |
| GET | `/post/<slug>/` | View a post |
| GET, POST | `/admin-login/` | Staff sign-in |
| GET | `/admin-logout/` | Sign out |
| GET | `/dashboard/` | Staff dashboard |
| GET, POST | `/dashboard/new/` | Create a post |
| GET, POST | `/dashboard/edit/<id>/` | Edit a post |
| GET, POST | `/dashboard/delete/<id>/` | Confirm and delete a post |
| GET | `/admin/` | Django admin |

## Future Improvements

- Add post search, categories, and tags
- Add reader accounts and comments
- Create a REST API for posts
- Add automated tests
- Add a `requirements.txt` file
- Prepare production deployment settings and documentationlogSphere

BlogSphere is a Django blogging platform where visitors can browse posts and staff can manage blog content through a protected dashboard.

## Features

- Browse posts with pagination (six posts per page)
- View individual posts using unique URL slugs
- Display post images, authors, and publication dates
- Staff sign-in and protected content dashboard
- Create, edit, and delete posts
- Django admin interface

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Django templates

## Installation

1. Clone the repository and enter the project directory:

   ```bash
   git clone <repository-url>
   cd blogsphere
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   **Windows PowerShell**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install django pillow
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a staff account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

Visit <http://127.0.0.1:8000/> to browse the site. Staff can sign in at <http://127.0.0.1:8000/admin-login/>. The Django admin is available at <http://127.0.0.1:8000/admin/>.

## Database Setup

BlogSphere uses SQLite by default. The database is stored in `db.sqlite3` in the project root.

After changing the models, create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Routes

These are Django web routes; the project does not currently provide a REST API.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Browse paginated posts |
| GET | `/post/<slug>/` | View a post |
| GET, POST | `/admin-login/` | Staff sign-in |
| GET | `/admin-logout/` | Sign out |
| GET | `/dashboard/` | Staff dashboard |
| GET, POST | `/dashboard/new/` | Create a post |
| GET, POST | `/dashboard/edit/<id>/` | Edit a post |
| GET, POST | `/dashboard/delete/<id>/` | Confirm and delete a post |
| GET | `/admin/` | Django admin |

## Future Improvements

- Add post search, categories, and tags
- Add reader accounts and comments
- Create a REST API for posts
- Add automated tests
- Add a `requirements.txt` file
- Prepare production deployment settings and documentation
