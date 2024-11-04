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
        print("3. Cadastrar Instrutor(a)")
        print("4. Cadastrar Plano")
        print("5. Editar Plano")
        print("6. Excluir Plano")
        print("7. Verificar disponibilidade do equipamento")
        print("8. Disponibilidade do(a) instrutor(a)")
        print("9. Criar turma")
#        print("10. Cadastrar equipamento")
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
            nome = input("Nome do(a) Instrutor(a): ")
            especialidade = input("Especialidade do instrutor(a): ")
            horario_trabalho = input("Trabalha em qual período? | Digite uma das opções abaixo:\nManhã, Tarde ou Noite? ")
            crud.cadastrar_instrutor(db, nome, especialidade, horario_trabalho)

        elif escolha == "4":
            tipo = input("Digite o tipo de plano desejado conforme as opções abaixo:\nMensal, Trimestral ou Anual? ")
            preco = int(input("Preço do Plano: "))
            crud.cadastrar_plano(db, tipo, preco)

        elif escolha == "5":
            plano_id = int(input("ID do Plano: "))
            tipo = input("Novo tipo do Plano (ou Enter para manter): ")
            preco = input("Novo preço do Plano (ou Enter para manter): ")
            crud.editar_plano(db, plano_id, tipo if tipo else None, int(preco) if preco else None)

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

        #elif escolha == "10":
#            nome = input("Nome do equipamento: ")   
#            quantidade = int(input("Quantidade desse equipamento: "))  
#            manutencao = input("Data da última manutenção feita no equipamento: ") 
#            crud.cadastrar_equipamento(db, nome, quantidade, manutencao)  

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    db.close()  # Fecha a sessão ao sair

if __name__ == "__main__":
    main()
