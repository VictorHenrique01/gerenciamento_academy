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
def cadastrar_instrutor(db: Session, nome: str, especialidade: str, horario_trabalho: str):
    try:
        instrutor = Instrutor(nome=nome, especialidade = especialidade, horario_trabalho=horario_trabalho)
        db.add(instrutor)
        db.commit()
        db.refresh(instrutor)
        print("Instrutor cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar instrutor: {e}")

# Em crud.py

def consultar_disponibilidade_instrutor(db: Session, periodo: str):
    try:
        instrutores = db.query(Instrutor).filter(Instrutor.horario_trabalho == periodo).all()
        if instrutores:
            print(f"Instrutores disponíveis no período {periodo}:")
            for instrutor in instrutores:
                print(f"- {instrutor.nome} (Especialidade: {instrutor.especialidade})")
        else:
            print(f"Nenhum instrutor disponível no período {periodo}.")
    except Exception as e:
        print(f"Erro ao consultar disponibilidade de instrutores: {e}")


# Gerenciar Planos (Criar, Editar, Remover)
def cadastrar_plano(db: Session, tipo: str, preco: int):
    try:
        plano = Plano(tipo=tipo, preco=preco)
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
def criar_turma(db: Session, nome: str, horario: str, instrutor_id: int):
    try:
        turma = Turma(nome=nome, horario=horario, instrutor_id=instrutor_id)
        db.add(turma)
        db.commit()
        db.refresh(turma)
        print("Turma criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar turma: {e}")

# Controle de Equipamentos (CRUD)
def cadastrar_equipamento(db: Session, nome: str, quantidade: int, manutencao: str):
    try:
        equipamento = Equipamento(nome=nome, quantidade=quantidade, manutencao=manutencao)
        db.add(equipamento)
        db.commit()
        print("Equipamento cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar equipamento: {e}")

# Em crud.py

def consultar_equipamento(db: Session, nome_equipamento: str):
    try:
        equipamento = db.query(Equipamento).filter(Equipamento.nome == nome_equipamento).first()
        if equipamento:
            if equipamento.quantidade > 0:
                print(f"Equipamento '{equipamento.nome}' disponível: {equipamento.quantidade} unidade(s) disponível(eis).")
            else:
                print(f"Equipamento '{equipamento.nome}' está indisponível no momento.")
        else:
            print("Equipamento não encontrado.")
    except Exception as e:
        print(f"Erro ao consultar equipamento: {e}")


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
