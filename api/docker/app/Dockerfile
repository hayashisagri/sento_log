FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update
RUN apt-get install -y libgdal-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD .. /code/