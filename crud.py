# crud.py
from sqlalchemy.orm import Session
from entidades import Aluno, Instrutor, Plano, Equipamento, Turma

# CRUD para Aluno
def criar_aluno(db: Session, nome: str, idade: int, plano_id: int):
    aluno = Aluno(nome=nome, idade=idade, plano_id=plano_id)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

def consultar_alunos(db: Session):
    return db.query(Aluno).all()

def atualizar_aluno(db: Session, id: int, nome: str = None, idade: int = None, plano_id: int = None):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if aluno:
        if nome:
            aluno.nome = nome
        if idade:
            aluno.idade = idade
        if plano_id:
            aluno.plano_id = plano_id
        db.commit()
        db.refresh(aluno)
    return aluno

def excluir_aluno(db: Session, id: int):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if aluno:
        db.delete(aluno)
        db.commit()
    return aluno