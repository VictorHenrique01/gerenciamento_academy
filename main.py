# main.py
from sqlalchemy.orm import Session
from database import SessionLocal  # Importa a função de sessão
import crud


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
        print("7. Verificar disponibilidade do equipamento")
        print("8. Disponibilidade do instrutor")
        print("9. Criar turma")
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
            especialidade = input("Especialidade do instrutor: ")
            horario_trabalho = input("Trabalha em qual período? | Insira uma das opções: Manhã, Tarde ou Noite? ")
            crud.cadastrar_instrutor(db, nome, especialidade, horario_trabalho)

        elif escolha == "4":
            nome = input("Tipo de Plano seria Mensal, Trimestral ou Anual? ")
            preco = float(input("Preço do Plano: "))
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
            nome_equipamento = input("Nome do Equipamento para verificar disponibilidade: ")
            crud.consultar_equipamento(db, nome_equipamento)


        elif escolha == "8":
            periodo = input("Qual período deseja verificar a disponibilidade dos instrutores? (Manhã, Tarde ou Noite): ").capitalize()
            crud.consultar_disponibilidade_instrutor(db, periodo)

        elif escolha == "9":
            nome = input("Nome da Turma conforme a sua especialidade: ")
            horario = input("Horário da aula: ")
            instrutor_id = int(input("ID do instrutor: "))
            crud.criar_turma(db, nome, horario, instrutor_id)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    db.close()  # Fecha a sessão ao final

if __name__ == "__main__":
    main()
