FROM arm32v6/python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
  # dependencies for building Python packages
  && apk add --no-cache build-base \
  # psycopg2 dependencies
  && apk add --no-cache postgresql-dev \
  # Translations dependencies
  && apk add --no-cache gettext \
  && apk add --no-cache libffi-dev 

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
