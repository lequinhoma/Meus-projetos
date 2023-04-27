import random
def jogar():
    
    titulo()

    numero_secreto = random.randint (1,100)
    pontos = 1000
    
    dificuldade = escolher_dificuldade()


    for rodada in range (1, dificuldade + 1):

        print (f"Tentativa {rodada} de {dificuldade}")

        numero_usuario = input("Digite o seu número de 1 a 100: \n")

        chute = int(numero_usuario)

        print("Você digitou:", numero_usuario)
        
        parametros(chute,numero_secreto)
 
        pontos_perdidos = abs (numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    
    
    print (pontos)
    
    tchau(pontos,numero_secreto)


def titulo ():
    print("*" * 50)
    print ("Bem vindo ao jogo de advinhação !")
    print("*" * 50)
def escolher_dificuldade():
        print ("Escolha sua dificuldade0")
        print ("""
            Fácil? Digite 1
            Médio? Digite 2
            Difícil? Digite 3""")
        
        nivel = int(input("Digite a dificuldade:\n"))



        if nivel == 1:
            total_de_tentativas = 20
        elif nivel == 2:
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5
        return total_de_tentativas


def parametros(chute,numero_secreto,dificuldade):

    while chute < numero_secreto:
        print ("Chute um numero maior")
        break
    else:
        print ("você errou")
    
        print ("Chute um numero menor")
    if chute == numero_secreto:
            print ("VOCÊ ACERTOU, MUITO FODA")
            
            exit()
    elif (dificuldade == 0) and chute != numero_secreto:
        print ("Você perdeu, que pena")
        exit()
                           
def tchau(pontos,numero_secreto):
    print (f"Sua pontuação foi:\n{pontos} pontos")
    print ("O numero secreto era >>>", numero_secreto, "!!!")
    print("Tchau")

if (__name__ == "__main__"):
    jogar()
