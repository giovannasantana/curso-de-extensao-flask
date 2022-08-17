from flask import Flask, render_template, request
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
@app.route("/teste/")
@app.route("/teste/<variavel>")
# Se a variavel não for passada carrega normalmente
def funcao_teste(variavel=""):
    # Passando informacoes através do format
    return "Nova rota teste: {}".format(variavel), 200


# Rota de formulario
@app.route("/form")
def form():
    return render_template("form.html"), 200


app.run()
