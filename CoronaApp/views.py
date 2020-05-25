from django.shortcuts import render
import requests, json


def home(request):
    labels = []
    confirmados_tl = []
    mortestotais_tl = []
    recuperados_tl = []
    ativos_tl = []
    info = {}
    payload = {}
    headers = {}

    urlbrasil = "https://api.covid19api.com/total/dayone/country/brazil"

    html = requests.request("GET", urlbrasil, headers=headers, data=payload)

    brasil = json.loads(html.content)

    for dados in brasil:
        confirmados_tl.append(dados['Confirmed'])
        mortestotais_tl.append(dados['Deaths'])
        recuperados_tl.append(dados['Recovered'])
        ativos_tl.append(dados['Active'])
        dt = dados['Date'].split("T")[0]
        ano = dt.split("-")[0]
        mes = dt.split("-")[1]
        dia = dt.split("-")[2]
        fim = dia + "/" + mes + "/" + ano
        labels.append(fim)

    info['labels'] = labels
    info['confirmados_tl'] = confirmados_tl
    info['mortestotais_tl'] = mortestotais_tl
    info['recuperados_tl'] = recuperados_tl
    info['ativos_tl'] = ativos_tl
    info['casostotais'] = confirmados_tl[-1]
    info['mortestotais'] = mortestotais_tl[-1]
    info['recuperados'] = recuperados_tl[-1]
    info['ativos'] = ativos_tl[-1]

    return render(request, 'CoronaApp/piloto.html', info)


def faq(request):
    return render(request, 'CoronaApp/faq.html')
