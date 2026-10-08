from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
  stmt = select(Livro)
  for l in session.scalars(stmt):
    print(l.titulo, l.autor.nome, l.disponivel)

def listar_livros_disponiveis(session):
  stmt = select(Livro).where(Livro.disponivel == True)
  for l in session.scalars(stmt):
    print(l.titulo)

def buscar_livros_por_titulo(session, trecho):
  stmt = select(Livro).where(Livro.titulo.contains(trecho))
  for l in session.scalars(stmt):
    print(l.titulo)

def listar_livros_por_autor(session, nome_autor):
  stmt = select(Autor).where(Autor.nome == nome_autor)
  a = session.scalars(stmt).first()
  if a:
    for l in a.livros:
      print(l.titulo)