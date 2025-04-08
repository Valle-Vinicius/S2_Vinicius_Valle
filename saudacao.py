def saudacao():
    nome = input("Qual o seu nome? ")
    print("Olá, {nome}!")  

def escolha_opcao():
    print("Escolha uma opção:")
    print("1. Saudação")
    print("2. Sair")
    opcao = input("Digite sua opção: ")
    
    if opcao == '1':
        saudacao()
    elif opcao == '2'
        print("Saindo...") 
    else:
        print("Opção inválida.")
        escolha_opcao()

escolha_opcao()
