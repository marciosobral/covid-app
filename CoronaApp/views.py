from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def home(request):
    info = {}

    url = "https://www.worldometers.info/coronavirus/country/brazil/"
    url2 = "https://www.ibge.gov.br/explica/desemprego.php"

    html = requests.get(url)
    html2 = requests.get(url2)

    bs = BeautifulSoup(html.content, 'html.parser')
    bs2 = BeautifulSoup(html2.content, 'html.parser')

    taxa_desemprego = bs2.find_all('p', class_='variavel-dado')[2].get_text()
    casos_totais = bs.find_all('div', class_='maincounter-number')[0].get_text()
    mortes_totais = bs.find_all('div', class_='maincounter-number')[1].get_text()
    recuperados = bs.find_all('div', class_='maincounter-number')[2].get_text()

    casos_ativos = bs.find_all('div', class_='number-table-main')[0].get_text()
    casos_leves = bs.find_all('span', class_='number-table')[0].get_text()
    casos_graves = bs.find_all('span', class_='number-table')[1].get_text()

    info['taxadesemprego'] = taxa_desemprego
    info['casostotais'] = casos_totais
    info['mortestotais'] = mortes_totais
    info['recuperados'] = recuperados
    info['casosativos'] = casos_ativos
    info['casosleves'] = casos_leves
    info['casosgraves'] = casos_graves

    y_pos = list(range(len(casos_totais)))
    plt.bar(y_pos, taxa_desemprego[::-1], align='center', alpha=0.5)
    plt.xticks(y_pos, casos_totais[::-1], rotation=70)
    plt.ylabel('Total cases')
    plt.title('Persons affected by Corona virus')
    plt.savefig('Corona-analysis.png', dpi=600)
    plt.show()

    return render(request, 'CoronaApp/Piloto.html', info)
