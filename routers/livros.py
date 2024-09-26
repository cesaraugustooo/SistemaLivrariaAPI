from fastapi import APIRouter

from models.livro import Livro
from schemas.livros import *
from models.livro import Livro
router = APIRouter()

@router.get(path="/livros", response_model=livroReadAll)
def get_livros():
    livros = Livro.select()
    return {'livros': livros}

@router.get(path="/livros/{id}", response_model=LivroRead)
def get_livro(id: int):
    livros = Livro.get_or_none(Livro.id == id)
    return livros
@router.post(path="/livros", response_model=LivroRead)
def create_livro(livro: LivroCreate):
    criar = Livro.create(**livro.model_dump())
    return criar
@router.delete(path="/livros/{id}", response_model=LivroRead)
def delete_livro(id: int):
    livro = Livro.get_or_none(Livro.id == id)
    livro.delete_instance()
    return livro
@router.patch(path="/livros", response_model=LivroRead)
def update_livro(livro: LivroUpdate, id: int):
    livros = Livro.get_or_none(Livro.id == id)
    livros.nome = livro.nome
    livros.descricao = livro.descricao
    livros.preco = livro.preco
    livros.genero = livro.genero
    livros.edicao = livro.edicao
    livros.editora = livro.editora
    livros.publicacao = livro.publicacao
    livros.save()
    return livros