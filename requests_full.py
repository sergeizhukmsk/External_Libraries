import requests


# 1. Отправка GET-запроса
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)  # выводим текст ответа
    else:
        print(f"Ошибка: {response.status_code}")


# 2. Отправка POST-запроса с данными
def post_data(url, data):
    response = requests.post(url, json=data)
    print(response.json())  # выводим JSON-ответ


# 3. Использование сессии для сохранения состояния
def session_example(url):
    with requests.Session() as session:
        response = session.get(url)
        print(response.text)


def fetch_data(url):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        print('Вернуть данные в формате JSON')
        return response.json()  # Вернуть данные в формате JSON
    else:
        raise Exception(f"Ошибка запроса: {response.status_code}")


# Примеры вызова функций
get_data('https://mail.ru')
post_data('https://jsonplaceholder.typicode.com/posts', {'title':'foo', 'body':'bar', 'userId':1})
session_example('https://mail.ru')
data = fetch_data('https://api.github.com/users/sergeizhukmsk')
print(data)
