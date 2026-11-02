from flask_sqlalchemy import  SQLAlchemy
db =SQLAlchemy()
class AlunoModel(db.model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(200))
  @staticmethod
  def adicionar_aluno(nome):
    aluno = AlunoModel(nome=nome)
    db.session.add(aluno)
    db.session.commit()
  @staticmethod
  def listar_alunos():
    return [a.nome for a in AlunoModel.query.all()]
    

