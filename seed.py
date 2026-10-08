from models import Autor, Livro


def popular_banco(session):
  a1 = Autor(nome="autor 1", pais="brasil")
  a2 = Autor(nome="autor 2", pais="chile")
  a3 = Autor(nome="autor 3", pais="peru")
  l1 = Livro(titulo="livro 1", ano=2020, autor=a1, disponivel=True)
  l2 = Livro(titulo="livro 2", ano=2021, autor=a1, disponivel=False)
  l3 = Livro(titulo="livro 3", ano=2022, autor=a2, disponivel=True)
  l4 = Livro(titulo="livro 4", ano=2023, autor=a2, disponivel=False)
  l5 = Livro(titulo="livro 5", ano=2024, autor=a3, disponivel=True)
  l6 = Livro(titulo="livro 6", ano=2025, autor=a3, disponivel=True)
  session.add_all([a1, a2, a3, l1, l2, l3, l4, l5, l6])
  session.commit()