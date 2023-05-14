import requests
import json

# Define a URL que você deseja solicitar
url = 'https://api.hgbrasil.com/weather'

captura_campos = []

# Faz a solicitação GET
response = requests.get(url)

# Verifica o status code da resposta (200 significa que a solicitação foi bem-sucedida)
if response.status_code == 200:

    # Exibe o conteúdo da resposta
    # print(response.content)

    json_all = response.json()

    json_principal =  json_all["results"]
    # print(json_principal)

    captura_campos.append([json_principal["temp"],json_principal["description"],json_principal["currently"],json_principal["rain"],json_principal["city_name"]])
    # print(captura_campos)

    for campos in captura_campos:
        # print(campos)
        print("Temperatura atual: " + str(campos[0]) + "ºC,")
        print("Descrição da condição de tempo atual: " + str(campos[1]) + ",")
        print("Retorna se está de dia ou de noite: " + str(campos[2]) + ",")
        print("Volume de chuva em mm na última hora: " + str(campos[3]) + ",")
        print("Nome da cidade: " + str(campos[4]) + ".")

else:
    print('A solicitação falhou com o código de status:', response.status_code)
