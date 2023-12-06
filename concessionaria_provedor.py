from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

#Criado por  Rafael
carros = [{"modelo": "Carro1", "preco": 20000}, {"modelo": "Carro2", "preco": 25000}]
vendas = []

@app.route('/carros', methods=['GET'])
def obter_carros():
    return jsonify({"carros": carros})

@app.route('/vendas', methods=['GET'])
def obter_vendas():
    return jsonify({"vendas": vendas})
