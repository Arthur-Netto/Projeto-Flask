from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.secret_key = 'SECRET'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
db = SQLAlchemy(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    sobrenome: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def homepage():
    # Salvar do form no Banco de Dados caso for "POST" e retornar /login
    if request.method == "POST":
        usuario = User(
            nome = request.form["nome"],
            sobrenome = request.form["sobrenome"],
            email = request.form["email"],
            senha = request.form["senha"],
        )
        db.session.add(usuario)
        db.session.commit()
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

