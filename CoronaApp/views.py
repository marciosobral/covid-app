from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request):
    data = {}

    url = "https://www.worldometers.info/coronavirus/country/brazil/"
    html = requests.get(url)

    bs = BeautifulSoup(html.content, 'html.parser')

    casos_totais = bs.find_all('div', class_='maincounter-number')[0].get_text()
    mortes_totais = bs.find_all('div', class_='maincounter-number')[1].get_text()
    recuperados = bs.find_all('div', class_='maincounter-number')[2].get_text()

    casos_ativos = bs.find_all('div', class_='number-table-main')[0].get_text()
    casos_leves = bs.find_all('span', class_='number-table')[0].get_text()
    casos_graves = bs.find_all('span', class_='number-table')[1].get_text()

    data['casostotais'] = casos_totais
    data['mortestotais'] = mortes_totais
    data['recuperados'] = recuperados

    return render(request, 'CoronaApp/Piloto.html', data)
