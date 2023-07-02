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

# create migrations
docker-compose exec web aerich init-db
```