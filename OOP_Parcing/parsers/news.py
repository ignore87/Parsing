from bs4 import BeautifulSoup as bs
import requests
from modules.MainParser import MainParser

class News(MainParser):
    def __init__(self, url):
        self.url = url
        self.items_list = []
    
    def parse(self):
        response = requests.get(self.url)
        html = bs(response.content, 'html.parser')
        for el in html.select('#form_3 > div > ul > ul:nth-child(4) > li > label')[0]:
            self.items_list.append(el.text)
        return self.items_list
