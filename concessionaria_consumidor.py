import requests

#Criado por Rafael
base_url = 'http://localhost:5000'

def obter_carros():
    response = requests.get(f'{base_url}/carros')
    return response.json()["carros"]

def obter_vendas():
    response = requests.get(f'{base_url}/vendas')
    return response.json()["vendas"]
