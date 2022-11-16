# Проект: CI и CD проекта api_yamdb
### Пуш на GitHub
Запускаются тесты flake8
Тесты django pytest
### Пуш на DockerHub
Добавьте в Secrets GitHub Actions переменные окружения для аутентификации:
DOCKER_USERNAME
DOCKER_PASSWORD
### Деплой на сервер
Добавьте в Secrets GitHub Actions переменные окружения для подключения к серверу:
HOST - ip-адрес или доменное имя сервера
USER - имя пользователя для аутентификации по SSH на сервере
SSH_KEY - приватный ключ вашего компьютера, перед этим открытый должен быть размещен /home/<user>/.ssh/authorized_keys
PASSPHRASE - парольная фраза на приватный ключ

Добавьте в Secrets GitHub Actions переменные окружения для работы с базой данных:
DB_ENGINE - база данных
DB_NAME - имя БД
POSTGRES_USER - имя пользователя
POSTGRES_PASSWORD - пароль
DB_HOST - хост базы данных
DB_PORT - порт поключения к базе данных
эти данные хранятся в файле .env в домашнем каталоге
### Контейнер Docker
Запускаются три контейнера:
web - проект api_yamdb
db - база данных postgres проекта api_yamdb
nginx - веб-сервер
### Технологии
Python 3.7
Gunicorn 20.0.4
Django 2.2.16
Postgres 13
Nginx 1.21.3
Docker 20.10.20
docker compose v2.12.2 
### Первоначальный запуск проекта на сервере
Выполните по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py loaddata fixtures.json
```
### Авторы
Соломаха Владимир

### Сервер
Сервер: 158.160.19.142

![Build Status](https://github.com/VladimirSolomakha/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
