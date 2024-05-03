from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    # Salvar do form no Banco de Dados caso for "POST" e retornar /login
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template ("usuarios.html", nome_usuario = nome_usuario)

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)



    #Como Criar e Publicar um Site em Python com Flask Hashtag Programação minutagem 38:06 / 1:00:29

