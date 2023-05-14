import requests 
import json


url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
url2 = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/{}'


parametros = {}
resposta = requests.request("GET", url, params=parametros)
objetos = json.loads(resposta.text)
dados = objetos['dados']

len(dados)
dados[0]
id = []
for i in range(len(dados)):
  id.append(str(dados[i]['id']))
print(id[:1])

urls3 = []
for i in id[:1]:
    url3 = url2.format(i)
    urls3.append(url3)
    print(url3)


for i in urls3[:1]:
    Request = requests.get(i)
    conteudo  = Request.json()
    print(conteudo) 
