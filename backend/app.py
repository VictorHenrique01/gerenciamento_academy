# Arquivo principal do FastAPI
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import crud
# Importando as entidades para criar as tabelas no banco de dados
from entidades import Aluno, Instrutor, Plano, Equipamento, Turma, Treino
from fastapi.middleware.cors import CORSMiddleware

# Criando o banco de dados e tabelas
Base.metadata.create_all(bind=engine)
# Inicializando o FastAPI
app = FastAPI(title="Sistema de Gerenciamento de Academia", version="1.0.0")
# Adicionando o middleware CORS
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],  # Permite todas as origens
   allow_credentials=True,
   allow_methods=["*"],  # Permite todos os métodos HTTP
   allow_headers=["*"],  # Permite todos os cabeçalhos
)

from pydantic import BaseModel

class AlunoCreate(BaseModel):
   nome: str
   idade: int
   plano_id: int
# Dependência para criar uma sessão de banco de dados por requisição
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()
# Endpoints para Aluno
@app.post("/alunos/", status_code=201)
def cadastrar_aluno(nome: str, idade: int, plano_id: int, db: Session = Depends(get_db)):
   crud.cadastrar_aluno(db, nome, idade, plano_id)
   return {"mensagem": "Aluno cadastrado com sucesso!"}
@app.put("/alunos/{aluno_id}", response_description="Editar um aluno")
def editar_aluno(aluno_id: int, nome: str = None, idade: int = None, plano_id: int = None, db: Session = Depends(get_db)):
   crud.editar_aluno(db, aluno_id, nome, idade, plano_id)
   return {"mensagem": "Dados do aluno atualizados com sucesso!"}
@app.get("/alunos/{aluno_id}", response_description="Consultar um aluno pelo ID")
def consultar_aluno(aluno_id: int, db: Session = Depends(get_db)):
   return crud.consultar_aluno(db, aluno_id)
# Endpoints para Treino
@app.post("/treinos/", response_description="Criar um treino")
def criar_treino(tipo: str, aluno_id: int, instrutor_id: int, db: Session = Depends(get_db)):
   crud.criar_treino(db, tipo, aluno_id, instrutor_id)
   return {"mensagem": "Treino criado com sucesso!"}
@app.get("/treinos/{nome_treino}", response_description="Consultar treinos por tipo")
def consultar_tipo_treino(nome_treino: str, db: Session = Depends(get_db)):
   crud.consultar_tipo_treino(db, nome_treino)
   return {"mensagem": "Consulta de treino concluída"}
# Endpoints para Equipamentos
@app.post("/equipamentos/", response_description="Cadastrar um equipamento")
def cadastrar_equipamento(nome: str, quantidade: int, manutencao: str, db: Session = Depends(get_db)):
   crud.cadastrar_equipamento(db, nome, quantidade, manutencao)
   return {"mensagem": "Equipamento cadastrado com sucesso!"}
@app.get("/equipamentos/{nome_equipamento}", response_description="Consultar equipamento")
def consultar_equipamento(nome_equipamento: str, db: Session = Depends(get_db)):
   crud.consultar_equipamento(db, nome_equipamento)
   return {"mensagem": "Consulta de equipamento concluída"}
@app.delete("/equipamentos/{equipamento_id}", response_description="Excluir equipamento")
def excluir_equipamento(equipamento_id: int, db: Session = Depends(get_db)):
   crud.excluir_equipamento(db, equipamento_id)
   return {"mensagem": "Equipamento excluído com sucesso!"}
# Endpoints para Instrutores
@app.post("/instrutores/", response_description="Cadastrar um instrutor")
def cadastrar_instrutor(nome: str, especialidade: str, horario_trabalho: str, db: Session = Depends(get_db)):
   crud.cadastrar_instrutor(db, nome, especialidade, horario_trabalho)
   return {"mensagem": "Instrutor cadastrado com sucesso!"}
@app.get("/instrutores/{periodo}", response_description="Consultar disponibilidade de instrutores")
def consultar_disponibilidade_instrutor(periodo: str, db: Session = Depends(get_db)):
   crud.consultar_disponibilidade_instrutor(db, periodo)
   return {"mensagem": "Consulta de instrutores concluída"}
# Endpoints para Planos
@app.post("/planos/", response_description="Cadastrar um plano")
def cadastrar_plano(tipo: str, preco: int, db: Session = Depends(get_db)):
   crud.cadastrar_plano(db, tipo, preco)
   return {"mensagem": "Plano cadastrado com sucesso!"}
@app.put("/planos/{plano_id}", response_description="Editar um plano")
def editar_plano(plano_id: int, tipo: str = None, preco: int = None, db: Session = Depends(get_db)):
   crud.editar_plano(db, plano_id, tipo, preco)
   return {"mensagem": "Plano atualizado com sucesso!"}
@app.delete("/planos/{plano_id}", response_description="Excluir um plano")
def excluir_plano(plano_id: int, db: Session = Depends(get_db)):
   crud.excluir_plano(db, plano_id)
   return {"mensagem": "Plano excluído com sucesso!"}
# Endpoints para Turmas
@app.post("/turmas/", response_description="Criar uma turma")
def criar_turma(nome: str, horario: str, instrutor_id: int, db: Session = Depends(get_db)):
   crud.criar_turma(db, nome, horario, instrutor_id)
   return {"mensagem": "Turma criada com sucesso!"}
@app.get("/turmas/{turma_id}", response_description="Consultar uma turma")
def consultar_turma(turma_id: int, db: Session = Depends(get_db)):
   crud.consultar_turma(db, turma_id)
   return {"mensagem": "Consulta de turma concluída"}