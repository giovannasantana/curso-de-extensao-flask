from flask import Flask, render_template
import os
os.system('cls')

app = Flask("projeto")


@app.route("/")
def ola_mundo():
    # Criando variavel com meu nome
    nome = 'Giovanna'

    # Criando um array
    produtos = [
        {"nome": "Ração", "preco": 199.99},
        {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200


app.run()
