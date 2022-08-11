from flask import Flask, render_template
import os
os.system('cls')

app = Flask("projeto")


@app.route("/")
def ola_mundo():
    # Criando variavel com meu nome
    nome = 'Giovanna'

    return render_template("alo.html", n=nome), 200


app.run()
