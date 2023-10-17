# Тестовое задани от "Авангард"

## Описание
API для работы с конфиденциальными данными

Доработал от себя:
- Систему Аутентификации и Авторизации
- Каждая запись принадлежит пользователю, который добавил эту запись
- Удалить/Изменить можно только свои данные (так как без этого может произойти потеря всех данных)

## Технологии
- Python
- Flask
- SQLAlchemy
- Alembic
- PostgreSQL

## Установка
```bash
git clone git@github.com:RG1ee/avangard-test.git
cd avangard-test

# Настройка переменных окружений
cat env.sample > .env

# Запуск
docker compose up --build
# Или
docker-compose up --build
```

## Пример запросов

### Примечние!
Если истекла экспирация токена,\
то отправьте запрос на Endpoint - 2 для получения нового токена

### Enpoint 1 - /api/v1/users/registration
request:
```bash
curl -X POST -F \
    http://0.0.0.0:5000/api/v1/users/registration \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "username": "Avangard",
        "password": "AvangardTest"
    }'
```
response - HTTP 200 OK
```basj
{
    "message": "Success"
}
```

### Endpoint 2 - /api/v1/users/login
request:
```bash
curl -X POST \
    http://0.0.0.0:5000/api/v1/users/login \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "username": "Avangard",
        "password": "AvangardTest"
    }'
```
response - HTTP 200 OK
```bash
{
    access: "access_token"
}
```

### Endpoint 3 - /api/v1/data POST
request:
```bash
curl -X POST \
    http://0.0.0.0:5000/api/v1/data/ \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer access_token (Ответ из Endpoint - 2)'
    -d '{
        "name": "Secret Name",
        "data": "Top Secret Data"
    }'
```
response - HTTP 200 OK
```bash
{
    "id": 1,
    "name": "Secret Name",
    "data": "Top Secret Data"
}
```

### Endpoint 4 - /api/v1/data GET
request:
```bash
curl -X GET \
    http://0.0.0.0:5000/api/v1/data/?page=1&per_page=1 \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer access_token (Ответ из Endpoint - 2)'
```
response - HTTP 200 OK (Ответ будет в виде одной записи, так как значение per_page = 1. Если послать такой же запрос на `http://0.0.0.0:5000/api/v1/data/`, то ответом будут все записи)
```bash
{
    "id": 1,
    "name": "Secret Name",
    "data": "Top Secret Data"
}
```

### Endpoint 5 - /api/v1/data/<data_id> GET
request:
```bash
curl -X GET \
    http://0.0.0.0:5000/api/v1/data/1 \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer access_token (Ответ из Endpoint - 2)'
```
response - HTTP 200 OK
```bash
{
    "id": 1,
    "name": "Secret Name",
    "data": "Top Secret Data"
}
```

### Endpoint 6 - api/v1/data/<data_id> PUT
request:
```bash
curl -X PUT \
    http://0.0.0.0:5000/api/v1/data/1 \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer access_token (Ответ из Endpoint - 2)' \
    -d '{
        "name": "Rename Secret Name",
        "data": "Rename Top Secret Data"
    }'
```
response - HTTP 200 OK
```bash
{
    "Message": "Successful data update number 1"
}
```

### Endpoint 7 - api/v1/data/<data_id> DELETE
request:
```bash
curl -X DELETE \
    http://0.0.0.0:5000/api/v1/data/1 \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer access_token (Ответ из Endpoint - 2)'
```
response - HTTP 200 OK
```bash
{
    {"Message": "Successful deletion"}
}
```
