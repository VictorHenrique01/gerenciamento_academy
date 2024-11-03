# main.py
from sqlalchemy.orm import Session
from database import SessionLocal  # Importa a função de sessão
import crud
import entidades  # Importando o módulo entidades

def main():
    db = SessionLocal()  # Cria uma sessão para o banco de dados
    
    while True:
        print("\nBem-vindo ao Sistema de Gerenciamento de Academia")
        print("1. Cadastrar Aluno")
        print("2. Editar Dados do Aluno")
        print("3. Cadastrar Instrutor")
        print("4. Cadastrar Plano")
        print("5. Editar Plano")
        print("6. Excluir Plano")
        print("7. Testar Inserção e Consulta de Aluno")  # Nova opção para testar inserção
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Aluno: ")
            idade = int(input("Idade do Aluno: "))
            plano_id = int(input("ID do Plano: "))
            crud.cadastrar_aluno(db, nome, idade, plano_id)

        elif escolha == "2":
            aluno_id = int(input("ID do Aluno: "))
            nome = input("Novo Nome do Aluno (ou Enter para manter): ")
            idade = input("Nova Idade do Aluno (ou Enter para manter): ")
            plano_id = input("Novo ID do Plano (ou Enter para manter): ")
            crud.editar_aluno(db, aluno_id, nome if nome else None, int(idade) if idade else None, int(plano_id) if plano_id else None)

        elif escolha == "3":
            nome = input("Nome do Instrutor: ")
            idade = input("Idade do Instrutor: ")
            especialidade = input("Especialidade do instrutor: ")
            horario_trabalho = input("Trabalha em qual período? | Insira uma das opções: Manhã, Tarde ou Noite? ")
            crud.cadastrar_instrutor(db, nome, idade, especialidade, horario_trabalho)

        elif escolha == "4":
            nome = input("Nome do Plano: ")
            preco = int(input("Preço do Plano: "))
            crud.cadastrar_plano(db, nome, preco)

        elif escolha == "5":
            plano_id = int(input("ID do Plano: "))
            nome = input("Novo Nome do Plano (ou Enter para manter): ")
            preco = input("Novo preço do Plano (ou Enter para manter): ")
            crud.editar_plano(db, plano_id, nome if nome else None, int(preco) if preco else None)

        elif escolha == "6":
            plano_id = int(input("ID do Plano para excluir: "))
            crud.excluir_plano(db, plano_id)

        elif escolha == "7":
            # Testar inserção e consulta
            nome = input("Nome do Aluno (teste): ")
            idade = int(input("Idade do Aluno (teste): "))
            plano_id = int(input("ID do Plano (teste): "))
            crud.cadastrar_aluno(db, nome, idade, plano_id)
            print("Aluno cadastrado com sucesso!")

            # Consulta para verificar a inserção
            aluno = db.query(entidades.Aluno).filter(entidades.Aluno.nome == nome).first()
            if aluno:
                print(f"\nAluno encontrado no banco de dados: ID={aluno.id}, Nome={aluno.nome}, Idade={aluno.idade}, Plano ID={aluno.plano_id}")
            else:
                print("Erro: Aluno não encontrado no banco de dados.")

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    db.close()  # Fecha a sessão ao final

if __name__ == "__main__":
    main()
