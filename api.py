import requests

tListAdress = []

tListPostalCode = ['01153000','20050000','70714020']

for PostalCode in tListPostalCode:

    tURL = 'https://viacep.com.br/ws/{}/json/'.format(PostalCode)

    tRequest = requests.get(tURL)

    tAdress = tRequest.json()

    tListAdress.append([tAdress["cep"],tAdress["logradouro"],tAdress["complemento"],tAdress["uf"]])

for ListAdress in tListAdress:

    print(ListAdress)