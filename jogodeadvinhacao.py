import random
print("*" * 50)
print ("Bem vindo ao jogo de advinhação !")
print("*" * 50)

numero_secreto = random.randint (1,101)
pontos = 1000
nivel = int(input("Digite a dificuldade:\n"))


print ("Escolha sua dificuldade0")
print ("""Fácil? Digite 1
Médio? Digite 2
Difícil? Digite 3""")



if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range (1, total_de_tentativas + 1):

    print (f"Tentativa {rodada} de {total_de_tentativas}")

    numero_usuario = input("Digite o seu número de 1 a 100: \n")

    chute = int(numero_usuario)

    print("Você digitou:", numero_usuario)

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)
    maior_perto = (numero_secreto < chute <= numero_secreto + 10)
    menor_perto = (numero_secreto - 10 <= chute < numero_secreto)
    muito_perto = (numero_secreto < chute <= numero_secreto + 2 ) or (numero_secreto - 2 <= chute < numero_secreto)

    # simplificação das variáveis

    if (chute < 1 or chute > 100):
        print ("você deve digitar um numero entre 1 e 100")
        continue

    if acertou:
        print(f"Você acertou!!!")
        break
    elif muito_perto:
        print ("MEU DEUS, ESTÁ PELANDO. Continue tentando")

    elif menor_perto:
        print ("Você está muito perto, chute para mais!")

    elif maior_perto:
        print ("Você está muito perto! Chute para menos")

    elif maior:
        print('Chute para menos')

    elif menor:
        print('chute para mais')
        
    pontos_perdidos = abs (numero_secreto - chute)
    pontos = pontos - pontos_perdidos
    

else:
    print("Se fudeu")
    print (pontos)


print (f"Pontuação:{pontos} pontos")
print("Tchau")
