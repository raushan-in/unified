
## Introduction
Merge the hotel list from diffrent source.

### Technical Stack
- Python 3.7.0
- Django 3.0.6
- Django Rest Framework (DRF) 3.8.0
- geopy 1.3.0

### Steps to setup server.
- First, ensure that Python is installed. 
- install the poetry (dependency manager) using command
```shell 
pip install poetry
```
- Top directory of the project contains .tomal file. Open terminal on this directory and run command:
```shell 
poetry install
```
- Once the all dependencies get installed, create virtual environment by 
```shell 
poetry shell
``` 
- go to 'unified' directory.
- In this directory you will find a file 'manage.py'.
- To start backend server type below command in terminal:
```shell
python manage.py runserver
```
- open http://127.0.0.1:8000/ in a browser.


