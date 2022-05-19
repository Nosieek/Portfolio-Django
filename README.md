# Django Blog
Overview
----
This web application creates every basic blog site using Django. The site allows any logged in user to add posts, category. Any user can list all bloggers, all blogs, and detail for bloggers and blogs.


## Techsite
Django templates, forms etc, Bootstrap5, HTML5, SQLite

## Quick Start

To get this project up and running locally on your computer:

1.Prerequisites
  - [Python3](https://www.python.org/downloads/) Python 3.5 + 
  - [Python venv](https://docs.python.org/3/library/venv.html) Python Virtual Environments

  
   ```
   git clone https://github.com/Nosieek/Portfolio-Django.git
   python3 -m venv venv
   source venv/bin/activate 
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

Blog Page
:-------------------------:
![Screenshot 25-05-2022  User view of the blog](https://github.com/Nosieek/Portfolio-Django/blob/main/home_page/static/img/user_view.png)
![Screenshot 25-05-2022  Staff view of the blog](https://github.com/Nosieek/Portfolio-Django/blob/main/home_page/static/img/staff_view.png)