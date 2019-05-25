FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN apk update && \
  apk add --no-cache postgresql-libs zlib-dev openjpeg-dev tiff-dev && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip install pipenv && \
  pipenv install && \
  apk --purge del .build-deps

COPY . .

VOLUME /usr/src/app/static

CMD ["gunicorn", "-b", ":8000", "-w", "4", "--access-logfile=-", "backend.wsgi"]