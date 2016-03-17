FROM python

WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py test
