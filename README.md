# BlogSphere – Blogging Web Application

## Project Overview

BlogSphere is a Django-based blogging web application developed using Python, Django, HTML, CSS, and SQLite.

This project allows visitors to browse blog posts and read individual articles. Each post displays its title, content, author, publication date, and image.

The application also provides a protected staff dashboard where authorized staff members can log in and create, edit, and delete blog posts. Django Admin is also available to manage blog content.

The main objective of this project is to understand how a blogging website works and gain practical experience in Django web development, database management, and CRUD operations.

## Features

- Browse and view blog posts
- Display six blog posts per page using pagination
- View individual blog posts
- Open posts using unique URL slugs
- Display post images, authors, and publication dates
- Staff login and logout
- Protected staff dashboard
- Create new blog posts
- Edit existing blog posts
- Delete blog posts
- Django admin panel for content management

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Django
- **Database:** SQLite
- **Image Handling:** Pillow
- **Tools:** VS Code, Git, GitHub

## Project Structure

- `app1/` – Django application files
- `templates/` – HTML templates
- `static/` – CSS and static files
- `media/` – Uploaded blog images
- `manage.py` – Django management file
- `db.sqlite3` – SQLite database

## Installation

Clone or download the project from GitHub and open it in VS Code.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install django pillow
```

## Database Setup

Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a staff administrator account:

```bash
python manage.py createsuperuser
```

## How to Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the following URLs in your browser:

- **Website:** http://127.0.0.1:8000/
- **Staff Login:** http://127.0.0.1:8000/admin-login/
- **Django Admin:** http://127.0.0.1:8000/admin/

Staff members can log in to the dashboard to manage blog posts.

Press `Ctrl + C` in the terminal to stop the server.

## Application Routes

| URL | Description |
|---|---|
| `/` | Home page with blog posts |
| `/post/<slug>/` | Individual blog post |
| `/admin-login/` | Staff login |
| `/admin-logout/` | Staff logout |
| `/dashboard/` | Staff dashboard |
| `/dashboard/new/` | Create a new post |
| `/dashboard/edit/<id>/` | Edit a post |
| `/dashboard/delete/<id>/` | Delete a post |
| `/admin/` | Django admin panel |

## Future Improvements

- Add blog post search functionality
- Add categories and tags
- Allow readers to register and comment
- Add a REST API
- Improve the user interface
- Add automated testing
- Deploy the application online

## Learning Outcomes

Through this project, I learned how to:

- Build a web application using Python and Django
- Create and manage database models
- Perform CRUD operations
- Work with Django templates and views
- Implement staff authentication
- Manage blog images
- Use Git and GitHub for version control
