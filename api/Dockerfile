# pull official base image
FROM python:3.9-slim

# set work directory
ENV APP_HOME /api
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    git

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/base.txt .
COPY ./requirements/dev.txt .
RUN pip install --no-cache-dir -r dev.txt

CMD python manage.py runserver 0.0.0.0:8000 --settings=api.settings.dev

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/api/entrypoint.sh"]