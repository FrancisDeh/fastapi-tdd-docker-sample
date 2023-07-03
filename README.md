# fastapi-tdd-docker-sample
A sample project with docker, tdd and CI with Github Actions.
Find the course tutorial [here](https://testdriven.io/courses/tdd-fastapi/postgres-setup/)


```
docker-compose up -d --build

docker-compose logs web
```
```
docker-compose exec web-db psql -U postgres
# \c web_dev
# \c dt
# \q
```

```shell
# initialize aerich
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
# or use this preference now
docker-compose exec web python app/db.py

# create migrations
docker-compose exec web aerich init-db

docker-compose exec web aerich upgrade
```

```shell
docker-compose exec web python -m pytest
# or 
docker-compose exec web pytest
# or
docker-compose exec web python -m pytest -p no:warnings;

docker-compose down -v
```

```shell
docker-compose exec web python -m pytest --cov="."
docker-compose exec web python -m pytest --cov="." --cov-report html

docker-compose exec web flake8 .

# check what will be formatted
docker-compose exec web black . --check

docker-compose exec web black . --diff

# actually format
docker-compose exec web black .

docker-compose exec web isort . --check-only
docker-compose exec web isort . --diff
docker-compose exec web isort .
```