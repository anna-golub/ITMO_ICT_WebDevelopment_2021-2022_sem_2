FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/library_project
COPY . /code/

RUN pip install -r requirements.txt
