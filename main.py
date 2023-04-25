import jogodeadivinhacao2
import forca
import pedra_papel_tesoura

print ("*"*80)
print ("Escolha seu jogo!!!")
print ("*"*80)

print("""Escolha entre: 
      (A) Jogo da forca
      (B) Jogo de adivinhação
      (C)\"Pedra, papel e tesoura\"""")

jogo= input ("Qual jogo? (A, B ou C)\n")

if jogo == "A" or jogo == "a":
    print ("Jogando FORCA")
    forca.jogar_forca()
    exit()
    
elif jogo == "B" or jogo == "b":
    print ("jogando Adivinhação")
    jogodeadivinhacao2.jogar()
    exit()
    
elif jogo == "C" or jogo== "c":

    print ("Jogando \"Pedra, papel ou tesoura\"")
    pedra_papel_tesoura.game()
    
    exit()
    
    
else: print("Você não inseriu uma entrada válida")
