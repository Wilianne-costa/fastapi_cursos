
from typing import List
from fastapi import FastAPI
from schema import AlunoCriacaoSchema, AlunoSchema, UpdateSchema
from models import Aluno
from starlette import status


app = FastAPI()


##############################################################
# CRIAR ALUNO
##############################################################
@app.post(
    "/alunos",
    response_model=AlunoSchema,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_aluno(request: AlunoCriacaoSchema):
        aluno = Aluno(nome=request.nome, idade=request.idade, curso=request.curso)
        aluno.save()

        return aluno.to_mongo().to_dict()


##############################################################
# DELETAR ALUNO POR ID
##############################################################
@app.delete("/alunos/{id}", status_code=status.HTTP_200_OK)
def deletar_aluno(id:str):
    aluno=Aluno.objects(id=id)
    aluno.delete()

    return {"msg":"Objeto excluido"}


##############################################################
# EXIBIR ALUNO POR ID
##############################################################
@app.get(
    "/alunos/{id}",
    response_model=AlunoSchema,
    status_code=status.HTTP_200_OK
)
def listar_alunos_id(id: str):
    aluno = Aluno.objects(id=id).first()

    return aluno.to_mongo().to_dict()


##############################################################
# LISTAGEM DE ALUNOS + FILTROS
##############################################################
@app.get(
    "/alunos",
    response_model=List[AlunoSchema],
    status_code=status.HTTP_200_OK
)
def listar_alunos_nome(nome=None, idade=None, curso=None):
    alunos = Aluno.objects.all()

    if nome != None:
        alunos = alunos.filter(nome=nome)

    if idade != None:
        alunos= alunos.filter(idade=idade)

    if curso != None:
        alunos = alunos.filter(curso=curso)

    lista_alunos = []

    for aluno in alunos:
        lista_alunos.append(aluno.to_mongo().to_dict())

    return lista_alunos


##############################################################
# ATUALIZAR ALUNO POR ID
##############################################################
@app.patch(
    "/alunos/{id}",
    response_model=AlunoSchema,
    status_code=status.HTTP_200_OK
)
def aluno_patch(id: str, request: UpdateSchema):
    aluno = Aluno.objects(id=id)
    aluno.update(**request.dict(exclude_none=True))

    return aluno.first().to_mongo().to_dict()


##############################################################
# ATUALIZAR ALUNO POR ID todos os campos
##############################################################
@app.put(
    "/alunos/{id}",
    response_model=AlunoSchema,
    status_code=status.HTTP_200_OK)

def aluno_put(id:str, request:AlunoCriacaoSchema):
    aluno = Aluno(id=id,nome=request.nome, idade=request.idade, curso=request.curso)
    aluno=aluno.save()

    return aluno.to_mongo().to_dict()


