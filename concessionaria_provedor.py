
from flask import Flask, jsonify # type: ignore
from flask import request # type: ignore

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


# Criado por Vinicius
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


#Criado por Lucca
@app.route('/adicionar_carro', methods=['POST'])
def adicionar_carro():
    dados_carro = request.json
    modelo_carro = dados_carro.get("modelo")
    preco_carro = dados_carro.get("preco")

    if not modelo_carro or not preco_carro:
        return jsonify({"mensagem": "Modelo e preço são obrigatórios"}), 400

    carros.append({"modelo": modelo_carro, "preco": preco_carro})
    return jsonify({"mensagem": f"Carro {modelo_carro} adicionado com sucesso"}), 201

@app.route('/remover_carro', methods=['POST'])
def remover_carro():
    dados_remocao = request.json
    modelo_carro = dados_remocao.get("modelo")

    if not modelo_carro:
        return jsonify({"mensagem": "Modelo é obrigatório"}), 400

    carro_encontrado = next((carro for carro in carros if carro["modelo"] == modelo_carro), None)
    if carro_encontrado:
        carros.remove(carro_encontrado)
        return jsonify({"mensagem": f"Carro {modelo_carro} removido com sucesso"}), 200
    else:
        return jsonify({"mensagem": f"Carro com modelo {modelo_carro} não encontrado"}), 404

    if __name__ == '__main__':
        app.run(debug=True)