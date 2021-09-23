FROM python:3.8.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./loans_site /app/loans_site

# CMD ["python", "loans_site/manage.py", "runserver", "0.0.0.0:8000"]

# CMD python loans_site/manage.py migrate \
#     && python loans_site/manage.py initadmin \
#     && python loans_site/manage.py runserver 0.0.0.0:8000 --noreload

