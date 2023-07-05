# yamdb_final

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку (в диапазоне от одного до десяти). Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

Аутентификация по JWT-токену.
Поддерживает методы GET, POST, PUT, PATCH, DELETE.
Предоставляет данные в формате JSON.
Создан в команде из трех человек с использованием Git в рамках учебного курса Яндекс.Практикум.

## Стек технологий

![python version](https://img.shields.io/badge/Python-3.7-yellowgreen) 
![python version](https://img.shields.io/badge/Django-3.2-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-yellowgreen) 

## Ресурсы API YaMDb

* Ресурс auth: аутентификация.
* Ресурс users: пользователи.
* Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
* Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
* Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
* Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
* Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.


## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Olga07122007/infra_sp2.git
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

В корневой директории создать файл `.env`, согласно примеру:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```


## Запустить приложение в контейнерах:

*из директории `infra/`*
```
docker-compose up -d --build
```

Выполнить миграции:

*из директории `infra/`*
```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

*из директории `infra/`*
```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

*из директории `infra/`*
```
docker-compose exec web python manage.py collectstatic --no-input
```

## Заполнить БД тестовыми данными

Для заполнения базы использовать файл `fixtures.json`, в директории `infra_sp2`. Выполните команду:

```bash
docker-compose exec web python manage.py loaddata fixtures.json
```


## Документация к проекту

Документация для API после установки доступна по адресу 

```redoc/```
