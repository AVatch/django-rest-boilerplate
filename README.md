# django-rest-boilerplate
A Django + REST API Boilerplate code with a custom user object

### Pairs with the following repos
1. [AngularJS REST Boilerplate](https://github.com/AVatch/angularjs-rest-boilerplate)

### Motivation
This is a boilerplate template for a Django REST framework which implements a custom AbstractBaseUser
with support for Django Admin and basic class based generic serializers and views for viewing the account object.

This is intended to be compatible with an AngularJS Boilerplate Code and Ionic Boilerplate Code Sample

### Setup
1. Create a virtual env
```$ virtualenv env```
2. Source the environment
```$ source env/bin/activate```
3. Install the dependencies
```$(env) pip install -r requirements.txt```
4. Switch to the django project
```$(env) cd drb```
5. Sync the Database
```$(env) python manage.py migrate```
6. Create a superuser object
```$(env) python manage.py createsuperuser```
7. Run the server
```$(env) python manage.py runserver```


### Endpoints
Currently there are two main endpoints ```/admin``` and ```/api/v1```
