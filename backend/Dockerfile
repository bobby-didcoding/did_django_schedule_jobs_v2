FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get -y install netcat &&  apt-get -y install gettext

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r /code/requirements/Base.txt

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]