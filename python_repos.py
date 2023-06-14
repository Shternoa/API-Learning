import requests

# Создание вызова и сохранения ответа API

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code: ', r.status_code)

# Сохранение ответа
repos_dict = r.json()

# Обработка результатов
print(repos_dict.keys())
