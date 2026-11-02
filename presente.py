class AlunoPresenter:
  def __init__(self, view, model):
      self.view = view
      self.model = model

  def listar(self):
      alunos = self.model.listar_alunos()
      return self.view.render(alunos)

  def adicionar(self, nome):
      if nome.strip() == "":
          return self.view.render(self.model.listar_alunos())

      self.model.adicionar_aluno(nome)
      return self.view.redirect_home()
