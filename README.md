# FitnessSchedule

## Init

##### Destroy docker containers and volumes
```bash
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```

##### Docker (dev)
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose build
docker-compose up
Adress: http://localhost/
```


##### .env file
```bash
SECRET_KEY==change_me
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
```