import json

import html5lib
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.vinorus.ru/ru-RU/about/contacts.aspx')

page = response.text

soup = BeautifulSoup(page, 'html5lib')

content = soup.find(id='section-2030').find_all('div', class_='col-sm-4')

departament_info = []
result = []

json_structure = {
    0: 'Имя',
    1: 'Должность',
    2: 'Телефон',
    3: 'Почта'
}

for index, item in enumerate(content):
    for linebreak in item.find_all('br'):
        linebreak.extract()
    item = item.find('div').text.split('\n')
    departament_info.append([])
    for el in item:
        if el:
            departament_info[index].append(el)

for item in departament_info:
    person = {}
    for i in range(4):
        person.setdefault(json_structure[i], item[i])
    result.append(person)

output = json.dumps(result, sort_keys=False, indent=4, ensure_ascii=False)

with open('result.json', 'w', encoding='utf-8') as f:
    f.write(output)
