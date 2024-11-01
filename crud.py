# crud.py
from sqlalchemy.orm import Session
from entidades import Aluno, Instrutor, Plano, Equipamento, Turma

# CRUD para Aluno
def cadastrar_aluno(db: Session, nome: str, idade: int, plano_id: int):
    try:
        aluno = Aluno(nome=nome, idade=idade, plano_id=plano_id)
        db.add(aluno)
        db.commit()
        db.refresh(aluno)
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")

# Editar Dados do Aluno
def editar_aluno(db: Session, aluno_id: int, nome: str = None, idade: int = None, plano_id: int = None):
    try:
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if aluno:
            if nome:
                aluno.nome = nome
            if idade:
                aluno.idade = idade
            if plano_id:
                aluno.plano_id = plano_id
            db.commit()
            db.refresh(aluno)
            print("Dados do aluno atualizados com sucesso!")
        else:
            print("Aluno não encontrado.")
    except Exception as e:
        print(f"Erro ao editar aluno: {e}")

# Cadastrar Instrutor
def cadastrar_instrutor(db: Session, nome: str):
    try:
        instrutor = Instrutor(nome=nome)
        db.add(instrutor)
        db.commit()
        db.refresh(instrutor)
        print("Instrutor cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar instrutor: {e}")

# Gerenciar Planos (Criar, Editar, Remover)
def cadastrar_plano(db: Session, nome: str, preco: int):
    try:
        plano = Plano(nome=nome, preco=preco)
        db.add(plano)
        db.commit()
        db.refresh(plano)
        print("Plano cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar plano: {e}")

def editar_plano(db: Session, plano_id: int, nome: str = None, preco: int = None):
    try:
        plano = db.query(Plano).filter(Plano.id == plano_id).first()
        if plano:
            if nome:
                plano.nome = nome
            if preco:
                plano.preco = preco
            db.commit()
            db.refresh(plano)
            print("Plano atualizado com sucesso!")
        else:
            print("Plano não encontrado.")
    except Exception as e:
        print(f"Erro ao editar plano: {e}")

def excluir_plano(db: Session, plano_id: int):
    try:
        plano = db.query(Plano).filter(Plano.id == plano_id).first()
        if plano:
            db.delete(plano)
            db.commit()
            print("Plano excluído com sucesso!")
        else:
            print("Plano não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir plano: {e}")

# Reservar Aula Coletiva (Associação entre Aluno e Turma)
def reservar_aula(db: Session, aluno_id: int, turma_id: int):
    try:
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        turma = db.query(Turma).filter(Turma.id == turma_id).first()
        if aluno and turma:
            turma.alunos.append(aluno)  # Supondo que Turma tenha um relacionamento 'alunos'
            db.commit()
            print("Aula reservada com sucesso!")
        else:
            print("Aluno ou turma não encontrados.")
    except Exception as e:
        print(f"Erro ao reservar aula: {e}")

# Controle de Equipamentos (CRUD)
def cadastrar_equipamento(db: Session, nome: str, quantidade: int, manutencao: str):
    try:
        equipamento = Equipamento(nome=nome, quantidade=quantidade, manutencao=manutencao)
        db.add(equipamento)
        db.commit()
        print("Equipamento cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar equipamento: {e}")

def editar_equipamento(db: Session, equipamento_id: int, nome: str = None, quantidade: int = None, manutencao: str = None):
    try:
        equipamento = db.query(Equipamento).filter(Equipamento.id == equipamento_id).first()
        if equipamento:
            if nome:
                equipamento.nome = nome
            if quantidade:
                equipamento.quantidade = quantidade
            if manutencao:
                equipamento.manutencao = manutencao
            db.commit()
            print("Equipamento atualizado com sucesso!")
        else:
            print("Equipamento não encontrado.")
    except Exception as e:
        print(f"Erro ao editar equipamento: {e}")

def excluir_equipamento(db: Session, equipamento_id: int):
    try:
        equipamento = db.query(Equipamento).filter(Equipamento.id == equipamento_id).first()
        if equipamento:
            db.delete(equipamento)
            db.commit()
            print("Equipamento excluído com sucesso!")
        else:
            print("Equipamento não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir equipamento: {e}")
