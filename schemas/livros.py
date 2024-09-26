from pydantic import BaseModel


class LivroCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    genero: str
    editora: str
    edicao: str
    publicacao: str

class LivroRead(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    genero: str
    editora: str
    edicao: str
    publicacao: str

class LivroUpdate(BaseModel):
    nome: str
    descricao: str
    preco: float
    genero: str
    editora: str
    edicao: str
    publicacao: str
class livroReadAll(BaseModel):
    livros: list[LivroRead]

