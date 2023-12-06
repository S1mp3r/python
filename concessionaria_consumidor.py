import requests

#Criado por Rafael
base_url = 'http://localhost:5000'

def obter_carros():
    response = requests.get(f'{base_url}/carros')
    return response.json()["carros"]

def obter_vendas():
    response = requests.get(f'{base_url}/vendas')
    return response.json()["vendas"]


#Criado por Vinicius
def realizar_venda(modelo, quantidade):
    dados_venda = {"modelo": modelo, "quantidade": quantidade}
    response = requests.post(f'{base_url}/vender', json=dados_venda)

    if response.status_code == 201:
        print(response.json()["mensagem"])
    else:
        print(f"Erro {response.status_code}: {response.json()['mensagem']}")

def obter_carros():
    response = requests.get(f'{base_url}/carros')
    return response.json()["carros"]

def obter_vendas():
    response = requests.get(f'{base_url}/vendas')
    return response.json()["vendas"]

def adicionar_carro(modelo, preco):
    dados_carro = {"modelo": modelo, "preco": preco}
    response = requests.post(f'{base_url}/adicionar_carro', json=dados_carro)

    if response.status_code == 201:
        print(response.json()["mensagem"])
    else:
        print(f"Erro {response.status_code}: {response.json()['mensagem']}")
