from flask import Flask, render_template, request, redirect
from model import db, AlunoModel
from presenter import AlunoPresenter
from view import IAlunoView

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alunos.db"
db.init_app(app)

with app.app_context():
    db.create_all()

class AlunoView(IAlunoView):
    def render(self, alunos):
        return render_template("index.html", alunos=alunos)

    def redirect_home(self):
        return redirect("/")

view = AlunoView()
presenter = AlunoPresenter(view, AlunoModel)

@app.route("/")
def index():
    return presenter.listar()

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    return presenter.adicionar(nome)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
