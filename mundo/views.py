from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    BASE_URL = 'https://www.cnnbrasil.com.br/tudo-sobre/futebol-internacional/'
    response = requests.get(BASE_URL)

    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    notices = parsed_html.find_all('a')

    class Notices:
        def __init__(self, title, href, img):
            self.title = title
            self.href = href
            self.img = img

    obj_list = list()
    for notice in notices:
        if (str(notice.get('href')).rfind('https://www.cnnbrasil.com.br/esportes/futebol/') == 0 and
            len(notice.get('href')) > 76) and notice.select_one('img') is not None:
            notice = Notices(notice.text.strip().split('   ')[0], notice.get('href'),
                             notice.select_one('img').get('src'))
            obj_list.append(notice)

    return render(request, 'index.html', {'obj_list': obj_list})