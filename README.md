<div align=center>
  
  # [Django_Referal_System](https://github.com/aleksandrkomyagin/Django_Referal_System) <br> (Реализация тестового задания) <br>
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![Redis](https://img.shields.io/badge/REDIS-23009639?style=for-the-badge&logo=redis&logoColor=white&color=ff1709&)
  ![Celery](https://img.shields.io/badge/CELERY-23009639?style=for-the-badge&logo=redis&logoColor=white&)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


</div>


## Описание:
Реализовать простую реферальную систему. Минимальный интерфейс для тестирования

## Функциональные требования:
*	Авторизация по номеру телефона. Первый запрос на ввод номера телефона. Имитировать отправку 4хзначного кода авторизации(задержку на сервере 1-2 сек). Второй запрос на ввод кода 
*	Если пользователь ранее не авторизовывался, то записать его в бд 
*	Запрос на профиль пользователя
*	Пользователю нужно при первой авторизации нужно присвоить рандомно сгенерированный 6-значный инвайт-код(цифры и символы)
*	В профиле у пользователя должна быть возможность ввести чужой инвайт-код(при вводе проверять на существование). В своем профиле можно активировать только 1 инвайт код, если пользователь уже когда-то активировал инвайт код, то нужно выводить его в соответсвующем поле в запросе на профиль пользователя
*	В API профиля должен выводиться список пользователей(номеров телефона), которые ввели инвайт код текущего пользователя.
*	Реализовать и описать в readme Api для всего функционала
*	Создать и прислать Postman коллекцию со всеми запросами
*	Залить в сеть, чтобы удобнее было тестировать(например бесплатно на https://www.pythonanywhere.com или heroku)

## Опциональные задачи:
*	Интерфейс на Django Templates
*	Документирование апи при помощи ReDoc
*	Docker

## Стек:
*	Python
*	Django, DRF
*	PostgreSQL

## Описание проекта


Django_Referal_System - REST API проект на DRF, в котором представлена реферальная система, с возможностью активации инвайт-кода, как при регистрации, так и после нее.

## Пользовательские роли и права доступа

* **Аноним** — доступен эндпоинт регистрации `auth/signup/` и `auth/confirmation_signup/`.
* **Аутентифицированный пользователь** — доступны эндпоинты `users/me/`, `users/activate_invite_code/` и `users/change_me/`с помощью которых пользователь может получать список рефералов, создавать, удалять свой инвайт код, получать инвайт код по email другого пользователя, активировать инвайт код от других пользователей и обновлять токен соответственно.

## Алгоритм регистрации нового пользователя

* Пользователь отправляет POST-запрос на добавление нового пользователя на эндпоинт `/api/v1/auth/signup/`. В запросе нужно указать номер телефона. 
* После получения кода подтверждения нужно отправить POST-запрос на `/api/v1/auth/confirmation_signup/`. В запросе нужно указать номер телефона и код подтверждения.
* При успешной регистрации пользователь получит токен доступа.
  

## Алгоритм активации инвайт кода

* Пользователь отправляет POST-запрос с кодом к эндпоинту  `/api/v1/users/activate_invite_code/`.
* В случае валидности предоставленного кода создаётся связь в БД между текущим пользователем и ползователем, предоставившим код.

<details>
  <summary>
    <h2>Запуск проекта на локальном сервере</h2>
  </summary>



> Для MacOs и Linux вместо python использовать python3
> Для запуска проекта на Windows потребуется установить вирутальную машину для запуска Redis.

1. Клонировать репозиторий.
   ```
   $ git@github.com:aleksandrkomyagin/django_referal_system.git
   ```
2. Cоздать и активировать виртуальное окружение, установить зависимости:
   - **pip**

     ```
      $ python -m venv venv
     ```
    
    Для Windows:
    ```
      $ source venv/Scripts/activate
    ```
    Для MacOs/Linux:
    ```
      $ source venv/bin/activate
    ```

    ```
    (venv) $ cd backend
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```
    - **poetry**
    ```
    (venv) $ cd backend
    poetry install
    ```
  
5. Создать файл .env в корневой папке проекта и заполнить файл по шаблону. Для успешного подключения к Redis параметру DEV должен быть в значении True. Если нужно запустить кол с БД postgres, установить значение параметра DB_ENGINE в True.
 
    ```
    POSTGRES_USER = логин для подключения к базе данных
    POSTGRES_PASSWORD = пароль для подключения к БД
    DB_HOST = название сервиса (контейнера)
    DB_PORT = порт для подключения к БД
    POSTGRES_DB = имя базы данных
    DB_ENGINE = ДБ (postgres/sqlite3)
    DEBUG=True
    DEV = режим разработки (True/False)
    ```

6. Выполнить миграции:
    ```
    (venv) $ python manage.py migrate
    ```

7. Запустить сервер:
    ```
    (venv) $ python manage.py runserver
    ```

8. Запустить Celery в отдельном терминале. Для этого нужно активировать виртуальное окружение и ввести команду:
    ```
    (venv) $ python -m celery -A referal_system worker -l info -P eventlet
    ```

> После выполнения вышеперечисленных инструкций бэкенд проекта будет доступен по адресу http://127.0.0.1:8000/

> Подробная документация API доступна после запуска сервера по адресу http://127.0.0.1:8000/api/v1/schema/docs/ - Swagger
http://127.0.0.1:8000/redoc/ - Redoc

</details>

<details>
  <summary>
    <h2> Запуск проекта в контейнере. </h2>
  </summary>

1. В файле .env закомментируйте две строки: DB_HOST и DB_PORT. Параметр DEV установите в значение False.

2. Из каталога django_referal_system выполните команду:
    ```
    (venv) $ docker compose -f docker-compose.yml up --build
    ```
</details>

> После выполнения вышеперечисленных инструкций бэкенд проекта будет доступен по адресу http://referalsystem.ddns.net:8000

---
<div align=center>

## Контакты

[![Telegram Badge](https://img.shields.io/badge/-aleksandrkomyagin8-blue?style=social&logo=telegram&link=https://t.me/aleksandrkomyagin8)](https://t.me/aleksandrkomyagin8) [![Gmail Badge](https://img.shields.io/badge/-aleksandrkomyagin8@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:aleksandrkomyagin8@gmail.com)](mailto:aleksandrkomyagin8@gmail.com)

</div>
