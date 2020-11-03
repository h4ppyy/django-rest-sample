# django-rest-sample

## Development environment

```
python 3.6.8
windows 10
```
see "requirements.txt"

## let's start project

```
git clone https://github.com/h4ppyy/django-rest-sample
cd django-rest-sample

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

docker-compose up

python manage.py runserver 0.0.0.0:8000
```

### django rest framework  
http://localhost:8000/api/v1/books/  

### drf-yasg (redoc)
http://localhost:8000/redoc/  

### drf-yasg (swagger)
http://localhost:8000/swagger/  