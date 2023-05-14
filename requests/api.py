import requests

ListAdress     = []
ListPostalCode = ['01153000','20050000','70714020']

for PostalCode in ListPostalCode:

    URL     = 'https://viacep.com.br/ws/{}/json/'.format(PostalCode)
    Request = requests.get(URL)
    Adress  = Request.json()
    # print(tAdress) 
    ListAdress.append([Adress["cep"],Adress["logradouro"],Adress["complemento"],Adress["uf"]])

for ListAdres in ListAdress:

    print(ListAdres)