from flask import Flask, render_template
import os
os.system('cls')

# Instanciando um objeto
app = Flask("projeto")


# Criando uma rota raiz
@app.route("/")
# Declarando uma funcao
def ola_mundo():
    # Criando variavel com meu nome
    nome = 'Giovanna'

    # Criando um array
    produtos = [
        {"nome": "Ração", "preco": 199.99},
        {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200


# Criando uma nova rota teste
@app.route("/teste")
def funcao_teste():
    return "Nova rota teste", 200  # Código http da requisicao


app.run()
