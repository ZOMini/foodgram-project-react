```
Проект работает:
http://130.193.37.228:9003/
un: ee-2@ya.ru / pw: Vitaliya  -(superuser)
```
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://130.193.37.228:9003/api/docs/)
[![foodgram workflow](https://github.com/zomini/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/zomini/zomini/foodgram-project-react/actions/workflows/main.yml)

# «Продуктовый помощник»
Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
 
## Инструкции для деплоя проекта на сервере

Последующие инструкции помогут вам настроить проект: <br>

### 1) Docker

Для того, чтобы развернуть проект на вашем сервере, вам необходимо предварительно установить Docker. <br>
Инструкция по установке: https://docs.docker.com/engine/install/

### 2) Автодеплой

В 'Actions secrets' в настройках вашего проекта на GitHub внесите необходимые параметры сервера: <br>

```
DOCKER_PASSWORD - Пароль от DockerHub (для обновления образа на DockerHub)
DOCKER_USERNAME - Логин от DockerHub (для обновления образа на DockerHub)
HOST - Публичный ip адрес сервера
USER - Пользователь сервера
PASSPHRASE - Если ssh-ключ защищен фразой-паролем
SSH_KEY - Приватный ssh-ключ
SECRET_KEY
DEBUG
```

После успешного коммита и прохождения тестов ваш проект автоматически будет настроен на сервере. <br>

### При первом деплое

Запустите миграции при помощи следующей команды:

```
sudo docker-compose exec backend python manage.py makemigrations --noinput
sudo docker-compose exec backend python manage.py migrate --noinput
```

Для сбора статики запустите следующую команду:

```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```

Для создания суперпользователя запустите следующую команду:

```
sudo docker-compose exec backend python manage.py createsuperuser
```
Чтобы заполнить базу данных начальными данными списка ингридиетов выполните:

```
docker-compose exec -T backend python manage.py loaddata data/ingredients_1.json 
```

Создайте теги: завтрак, обед, ужин <br>
http://62.84.117.214:9003/api/docs/  - Redoc<br>

## Системные требования
### Python==3.9

## Стек
### Django
### gunicorn
Web-сервера работают в отдельных контейнере.
### PostgreSQL
База данных лежит в отдельном контейнере.
### nginx
Сервер работает в отдельном контейнере.
### Docker
При помощи docker-compose происходит распаковка четырех контейнеров: база данных, фрон/бэк-сервера и nginx-сервер. Используются совместные тома памяти.
### Django REST Framework
API разработан для работы JS
### Github Actions
Проект автоматически деплоится в случае успешного коммита
### Яндекс.Облако
