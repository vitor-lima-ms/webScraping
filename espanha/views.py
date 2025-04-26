from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.

def noticiasLaLiga(request):
    BASE_URL = 'https://www.cnnbrasil.com.br/tudo-sobre/laliga/'
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
            notice = Notices(notice.text.strip().split('   ')[0], notice.get('href'), notice.select_one('img').get('src'))
            obj_list.append(notice)

    return render(request, 'noticiasLaLiga.html', {'obj_list': obj_list})

def laLiga(request):
    BASE_URL = 'https://www.cnnbrasil.com.br/esportes/futebol/tabela-laliga/'
    response = requests.get(BASE_URL)

    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    table = parsed_html.select_one(
        'body > div.site__content > div.live__content.container > section > div > div > div.col--12.col__l--8.campeonato__pontos__corridos__table.has-games > div.table__info > table > tbody')
    table_splitted = table.text.split('\n')
    classification_list = list()
    for element in table_splitted:
        if element == '':
            continue
        classification_list.append(element)

    class Team:
        def __init__(self, pos, name, abrv, points, games, wins, draws, losses, goals_for, goals_against, goal_difference):
            self.pos = int(pos)
            self.name = name
            self.abrv = abrv
            self.points = points
            self.games = games
            self.wins = wins
            self.draws = draws
            self.losses = losses
            self.goals_for = goals_for
            self.goals_against = goals_against
            self.goal_difference = goal_difference

        def __str__(self):
            return f'{self.name}'

    obj_list = list()
    i = 0
    f = 11
    for _ in range(20):
        team = Team(
            classification_list[i:f][0],
            classification_list[i:f][1],
            classification_list[i:f][2],
            classification_list[i:f][3],
            classification_list[i:f][4],
            classification_list[i:f][5],
            classification_list[i:f][6],
            classification_list[i:f][7],
            classification_list[i:f][8],
            classification_list[i:f][9],
            classification_list[i:f][10]
        )

        obj_list.append(team)

        i += 11
        f += 11

    return render(request, 'laLiga.html', {'obj_list': obj_list})