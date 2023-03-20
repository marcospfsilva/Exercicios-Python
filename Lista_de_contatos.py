#Programa que gera uma lista de contatos, de acordo com nome e telefone adicionados pelo usuário

novo_contato = input("Quer adicionar um novo contato?: ")

while novo_contato == "SIM" or novo_contato == "sim":
    contatos = open("lista_contatos.txt", "a")
    
    nome_contato = input("Qual o nome?: ")
    numero_contato = input("Qual o número?: ")


    lista = list()
    lista.append('Nome: '+ nome_contato + '\n' 'Numero: ' + numero_contato + '\n'+'\n')
    
    contatos.writelines(lista)
    
    novo_contato = input("\nQuer adicionar um novo contato?: ")

    if novo_contato =='NAO' or novo_contato =='nao':
        contatos = open("lista_contatos.txt", "r")
        leitor_contatos = contatos.readlines()
        
        print("\nOk! Aqui está sua lista atual:\n")
        
        for i in leitor_contatos:
            i = i.rstrip('\n')
            print(i)
