from flask import Flask, render_template
import os
os.system('cls')

app = Flask("projeto")


@app.route("/")
def ola_mundo():
    return render_template("alo.html"), 200


app.run()
