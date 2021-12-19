import requests
from bs4 import BeautifulSoup as BS

getr = []

URL = 'https://istrek.com/ru/%d0%be-%d1%84%d0%b8%d1%80%d0%bc%d0%b5/'


def get_html():
    response = requests.get(URL)
    return BS(response.text, features = "html.parser")

html1 = get_html()
res = html1.select("#av_section_2 > div > div")[0]
res = res.stripped_strings

for i in res:
    getr.append(f'\n{i}\n')
    getr.append('*' * 30)
with open('info.txt', 'w',encoding='utf-8' ) as file:
    file.write(' '.join(getr))
