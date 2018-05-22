# usage
start flask  
```bash
python manage.py runserver
```
start celery  
```bash
celery worker -A app.celery -B -c 1 --loglevel=INFO
```
