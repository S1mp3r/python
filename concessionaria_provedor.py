from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

#Criado por Rafael
carros = [{"modelo": "Carro1", "preco": 20000}, {"modelo": "Carro2", "preco": 25000}]
vendas = []

@app.route('/carros', methods=['GET'])
def obter_carros():
    return jsonify({"carros": carros})

@app.route('/vendas', methods=['GET'])
def obter_vendas():
    return jsonify({"vendas": vendas})

#Criado por Vinicius
@app.route('/vender', methods=['POST'])
def realizar_venda():
    dados_venda = request.json
    modelo_carro = dados_venda.get("modelo")
    quantidade = dados_venda.get("quantidade")

    if not modelo_carro or not quantidade:
        return jsonify({"mensagem": "Modelo e quantidade são obrigatórios"}), 400

    carro_encontrado = next((carro for carro in carros if carro["modelo"] == modelo_carro), None)
    if carro_encontrado:
        valor_total = carro_encontrado["preco"] * quantidade
        vendas.append({"modelo": modelo_carro, "quantidade": quantidade, "valor": valor_total})
        return jsonify({"mensagem": f"Venda realizada com sucesso para {quantidade} unidades do modelo {modelo_carro}"}), 201
    else:
        return jsonify({"mensagem": f"Carro com modelo {modelo_carro} não encontrado"}), 404
