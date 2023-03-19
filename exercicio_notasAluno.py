#Programa que pega 4 notas de um aluno e retorna se ele foi aprovado, reprovado ou se ficou de recuperação.

lista_Nota = []
contador = 0
while contador < 4:
    nota = input("Digite a nota: ")
    lista_Nota.append(float(nota))
    contador = contador+1

soma = sum(lista_Nota)
media = soma/4

if media >=7:
    print("Parabéns, você passou! Sua nota foi {}".format(media))
elif media <5:
    print("Infelizmente você foi reprovado, sua nota foi {}".format(media))
else:
    print("Você ficou de recuperação, sua nota foi {}".format(media))