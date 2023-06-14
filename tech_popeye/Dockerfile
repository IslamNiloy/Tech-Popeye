FROM python:3

RUN pip install Django==4.2.1
RUN pip install django-jazzmin==2.6.0
RUN pip install Pillow==9.5.0
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install mysqlclient
COPY . . 

RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
