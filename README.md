# Django Blog
Basic blog site written in Django
----
This web application creates an very basic blog site using Django. The site allows any logged in user to add posts, category and will in future can add comment via a forms. Any user can list all bloggers, all blogs, and detail for bloggers and blogs (including comments for each blog).

## Quick Start

To get this project up and running locally on your computer:
1. Requirements
  - a Laptop
  - Text Editor or IDE (eg. vscode, PyCharm)
  - Python 3.0 +
  - Django 4.0+

2. Install Python and Pipenv, I recommend using a Python virtual environment.
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

3. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   source venv/bin/activate - (This is active virtual environment) 
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver
   ```
4. Open a browser to `http://127.0.0.1:8000/` or `http://localhost:8000/` to open the main project site which showing projects (On this moment is only one, can be more in future)
5. Register as a blog user, create a few test posts of each category
6. Open tab to `http://127.0.0.1:8000/blog` or `http://localhost:8000/blog` to see the blog site, with your new objects.

## Screenshots

 Authors Dashboard Page
:-------------------------:
![Screenshot 25-05-2022  User view of the blog](https://github.com/Nosieek/Portfolio-Django/blob/main/home_page/static/img/user_view.png)