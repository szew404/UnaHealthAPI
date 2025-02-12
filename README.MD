
# UnaHealthAPI

API for Una Health coding challenge


## Installation to run locally

Clone the repository

```bash
    mkdir unahealthAPI
    cd unahealthAPI
    git clone https://github.com/szew404/UnaHealthAPI.git .
```

Create a new .env.conf file inside /src/config/ and add:

```bash
DJANGO_ENV=prod
```

Create a new .env file in the root directory and include the following variables.

```bash
    DJANGO_SECRET_KEY='v$1y@d4u843#es4z+3j!%5i$gav2d@e%94h27mxq6ot&j)c-5-'
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0 testserver

    # PostgreSQL
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=db_name
    SQL_USER=db_user
    SQL_PASSWORD=db_password
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres

    # DB Docker
    NAME_DB=db_name
    USER_DB=db_user
    PASS_DB=db_password
    HOST_DB=localhost

    #RedisforCelery
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
```
    
Replace 'db_name', 'db_user' and 'db_password' with the credentials of your postgresSQL database.

Run the project using Docker Compose

```bash
  docker compose up --build
```

Access to a new terminal, then migrate and collecstatic using djpro https://djpro.readthedocs.io/en/latest/

```bash
  docker exec -it unahealthapi-web-1 bash
```

```bash
  djpro man makemigrations
  djpro man migrate
  djpro man collecstatic
```