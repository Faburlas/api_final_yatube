### Описание проекта:

Это API социальной сети yatube и его можно использовать для использования с frontend.
API поддерживает возможность получения jwt токена, работы с постами, комментариями, группами и подписками.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone ttps://github.com/Faburlas/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Redoc документация API:

Чтобы увидеть openAPI документацию нужно запустить проект и перейти на страницу:

```
python3 manage.py runserver
```

```
http://127.0.0.1:8000/redoc/
```

### Пример работы с API:

1)Получение jwt токенов:
Отправляем POST запрос на
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
c Body:
```
{
    "username": "user",
    "password": "password"
}
```
Ответом на такой запрос будет:
```
{
    "refresh": "какой-то токен",
    "access": "какой-то токен"
}
```

2)Получение списка постов:
Отправляем GET запрос на:
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответом на такой запрос будет:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
