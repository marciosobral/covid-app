from django.shortcuts import render
import requests, json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def home(request):
    dia_count = 0
    casos = []
    info = {}
    data = []

    url = "https://www.worldometers.info/coronavirus/country/brazil/"
    url2 = "https://api.covid19api.com/all"

    html = requests.get(url)

    payload = {}
    headers = {}

    response = requests.request("GET", url2, headers=headers, data=payload)

    daily = json.loads(response.content)

    bs = BeautifulSoup(html.content, 'html.parser')

    casos_totais = bs.find_all('div', class_='maincounter-number')[0].get_text()
    mortes_totais = bs.find_all('div', class_='maincounter-number')[1].get_text()
    recuperados = bs.find_all('div', class_='maincounter-number')[2].get_text()

    info['casostotais'] = casos_totais
    info['mortestotais'] = mortes_totais
    info['recuperados'] = recuperados

    for dados in daily:
        if dados['Country'] == "Brazil":
            casos.append(dados['Confirmed'])
            dia_count = dia_count + 1
            data.append(dia_count)

    plt.ylabel('Casos totais')
    plt.xticks(fontsize=10, rotation=45)
    plt.title('Covid19 Brazil')
    plt.plot(data, casos)

    plt.savefig('CoronaApp/static/CoronaApp/image/covidgraph.png', dpi=120)
    return render(request, 'CoronaApp/Piloto.html', info)
