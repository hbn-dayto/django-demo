Goal: Learn how to use the Django Web Framework by creating side projects that involve data manipulation:

Objective: Build a Poll Application:
- Public Site: Users can use polls to   vote on website
- Admin Site: Administration can update polls

Project Setup:

1) Create Git Repository
- git init [repo_name]

2) Setup Virtual Environment:
- virtual env [venv_name]

3) Activate Virtual Environment: 
 Windows Powershell:
- Scripts/activate.ps1

4) Download Django with pip
- python -m pip install Django 
# Check what version:
    - import django
    - print(django.get_version())

5) Configuration setup:
 - admin startproject [project_name]
 
 # Creates a root directory (container for project ) 

 6) Run Development Server
 - python manage.py runserver
#  runserver command starts the development server on the internal IP at port 8000.

# to change the server's port, pass it as a command-line argument:
- python manage.py runserver 8080


