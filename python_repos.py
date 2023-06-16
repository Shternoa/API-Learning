import requests

# Создание вызова и сохранения ответа API

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code: ', r.status_code)

# Сохранение ответа
repos_dict = r.json()
print('Total repositories: ', repos_dict['total_count'])

# Анализ информации о репозиториях
repos_dicts = repos_dict['items']
print('Repositories returned: ', len(repos_dicts))

# Анализ первого репозитория
# repos_dict = repos_dicts[1]
# print("\nKeys: ", len(repos_dict))
# for key in sorted(repos_dict.keys()):
#     print(key)
# # Обработка результатов
# print(repos_dict.keys())

# Прочитаем значения некоторых ключей
for repos_dict in repos_dicts:
    print("\nSelected information about first repository:")
    print('Name:', repos_dict['name'])
    print('Owner:', repos_dict['owner']['login'])
    print('Stars:', repos_dict['stargazers_count'])
    print('Repository:', repos_dict['html_url'])
    print('Created:', repos_dict['created_at'])
    print('Updated:', repos_dict['updated_at'])
    print('Description:', repos_dict['description'])
