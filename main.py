# main.py
from database import engine, Base
from entidades import Aluno, Instrutor, Plano, Equipamento, Turma

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")
