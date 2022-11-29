# Tech Stack
* [Django](https://www.djangoproject.com/)
* [Django REST](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)


# Local Demo

## Requirements

You need to install:
* [Docker](https://www.docker.com/)

## Clone the repo and install the packages

    $ git clone https://github.com/OthLah001/heros-backend.git
    $ cd heros-backend
    $ docker-compose build
    $ docker-compose up
    
  Now open a new terminal and execute the following commands:
    
    $ docker exec -it backend_heros_container /bin/bash
    $ python manage.py migrate

## Run the server

    $ docker-compose up
