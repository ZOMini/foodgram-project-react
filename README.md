Адрес для проверки:<br>
http://51.250.106.203/ <br>
ee-2@ya.ru 90210 (superuser)<br>

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
DOCKER_PASSWORD - Пароль от DockerHub (для обновления образа на DockerHub) <br>
DOCKER_USERNAME - Логин от DockerHub (для обновления образа на DockerHub) <br>
HOST - Публичный ip адрес сервера <br>
USER - Пользователь сервера <br>
PASSPHRASE - Если ssh-ключ защищен фразой-паролем <br>
SSH_KEY - Приватный ssh-ключ <br>
TELEGRAM_TO - ID телеграм-аккаунта (для оправки уведомления об успешном деплое) <br>
TELEGRAM_TOKEN - Токен бота (для оправки уведомления об успешном деплое) <br>
```

После успешного коммита и прохождения тестов ваш проект автоматически будет настроен на сервере. <br>

### При первом деплое

Запустите миграции при помощи следующей команды:

```
sudo docker-compose exec web python manage.py makemigrations --noinput
sudo docker-compose exec web python manage.py migrate --noinput
```

Для сбора статики запустите следующую команду:

```
sudo docker-compose exec web python manage.py collectstatic --noinput
```

Для создания суперпользователя запустите следующую команду:

```
sudo docker-compose exec web python manage.py createsuperuser
```

Создайте теги: завтрак, обед, ужин

## Системные требования
### Python==3.9

## Стек
### Django
### gunicorn
Web-сервер работает в отдельном контейнере.
### PostgreSQL
База данных лежит в отдельном контейнере.
### nginx
Сервер работает в отдельном контейнере.
### Docker
При помощи docker-compose происходит распаковка трёх контейнеров: база данных, web-сервер и nginx-сервер. Используются совместные тома памяти.
### Django REST Framework
API разработан для работы JS
### Github Actions
Проект автоматически деплоится в случае успешного коммита
### Яндекс.Облако
