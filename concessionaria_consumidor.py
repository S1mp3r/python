import requests  # type: ignore

# Criado por Rafael
base_url = 'http://localhost:5000'


def obter_carros():
    response = requests.get(f'{base_url}/carros')
    return response.json()["carros"]


def obter_vendas():
    response = requests.get(f'{base_url}/vendas')
    return response.json()["vendas"]


# Criado por Vinicius
def realizar_venda(modelo, quantidade):
    dados_venda = {"modelo": modelo, "quantidade": quantidade}
    response = requests.post(f'{base_url}/vender', json=dados_venda)

    if response.status_code == 201:
        print(response.json()["mensagem"])
    else:
        print(f"Erro {response.status_code}: {response.json()['mensagem']}")


def adicionar_carro(modelo, preco):
    dados_carro = {"modelo": modelo, "preco": preco}
    response = requests.post(f'{base_url}/adicionar_carro', json=dados_carro)

    if response.status_code == 201:
        print(response.json()["mensagem"])
    else:
        print(f"Erro {response.status_code}: {response.json()['mensagem']}")


# Criado por Lucca
def remover_carro(modelo):
    dados_remocao = {"modelo": modelo}
    response = requests.post(f'{base_url}/remover_carro', json=dados_remocao)

    if response.status_code == 200:
        print(response.json()["mensagem"])
    else:
        print(f"Erro {response.status_code}: {response.json()['mensagem']}")


if __name__ == '__main__':
    carros = obter_carros()
    vendas = obter_vendas()

    print("Carros disponíveis:")
    for carro in carros:
        print(f"Modelo: {carro['modelo']}        Preço: {carro['preco']}")

    print("\nVendas realizadas:")
    for venda in vendas:
        print(
            f"Modelo: {venda['modelo']}        Quantidade: {venda['quantidade']}          Valor: {venda['valor']}")

    # Adicionar um novo carro
    adicionar_carro("Porshe", 3000000)

    # Faz a venda de um carro do estoque
    realizar_venda("Chevrolet", 200000)

    # Remover um carro do estoque
    remover_carro("Chevrolet")
