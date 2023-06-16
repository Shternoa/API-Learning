import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
names, plot_dicts = [], []
for repos_dict in repos_dicts:
    names.append(repos_dict['name'])
    plot_dict = {
        'value': repos_dict['stargazers_count'],
        'label': repos_dict['description'],
        'xlink': repos_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Анализ первого репозитория
# repos_dict = repos_dicts[1]
# print("\nKeys: ", len(repos_dict))
# for key in sorted(repos_dict.keys()):
#     print(key)
# # Обработка результатов
# print(repos_dict.keys())

# Построенеи визуализации
repo_style = LS('#441166', base_style=LCS)
repos_config = pygal.Config()
repos_config.x_label_rotation = 45
repos_config.show_legend = False
repos_config.title_font_size = 24
repos_config.label_font_size = 14
repos_config.major_label_font_size = 18
repos_config.truncate_label = 15
repos_config.show_y_guides = False
repos_config.width = 1000
tops = pygal.Bar(repos_config, style=repo_style)
tops.title = ('Python Projects')
tops.x_labels = names

tops.add('', plot_dicts)
tops.render_to_file('python_repos_4_5.svg')

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
