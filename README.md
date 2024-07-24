# Приложение для создания меню

Все команды написаны для shell

1. Скачать репозиторий выполнив команду:
```shell
git clone https://github.com/AlexeyRybicky/menu_app.git
```

2. Перейдите в скаченый каталог automatic-mailing-service
3. Внутри каталога создайте файл с переменными окружения(.env)  для работы проекта, за образец возьмите содержимое файла .env.template
4. Что бы запустить проект с помощью Docker выполните команду:
```shell
docker compose -f docker-compose.yml up --build
```
5. Перейдите в контейнер с приложением и создайте суперпользователя
```shell
docker exec -it automatic-mailing-service-app-1 /bin/bash

python manage.py createsuperuser
```

6. Для создания  меню перейдите по адресу http://localhost:8000/admin/

7. Созданные меню будут отображаться в главной странице http://localhost:8000