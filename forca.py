import random

    
def jogar_forca():
    
    imprime_mensagem_abertura()
    
    palavra_chave = carrega_palavra_secreta()

    letras_acertadas = inicializar_letras_acertadas(palavra_chave) 
    #parametro da função, vai substituir o parametro láááá embaixo
    
    print (letras_acertadas)
    
    enforcado = False
    acertou = False
    erros = 0
    
    while (not enforcado and not acertou):
        chute = pede_chute()
                
        if (chute in palavra_chave):
          marca_chute_correto(chute,letras_acertadas,palavra_chave)
        else:
            erros +=1 
        acertou = ("_" not in letras_acertadas)
        enforcado = erros == 6
        print (letras_acertadas)
        print (f"Você ainda tem {6 - erros} chances")
            
    if acertou:
        ganhador()
    
    
    else: 
    
        perdedor()
        

    
def imprime_mensagem_abertura():
    print ("*" * 80)
    print ("*"*26, "bem vindo ao jogo de forca", "*"*26)
    print ("*"*80)

def carrega_palavra_secreta():
        arquivo = []
        
        with open("palavras.txt") as lista:
            for x in lista:
                x = x.strip()
                arquivo.append(x)

            
            #x é um valor abstrato do que eu vou pegar dentro do arquivo e jogar pra lista
            
        numero = random.randrange(0,len(arquivo))
        palavra_chave = arquivo[numero].upper()
        return palavra_chave #para retornar lá pra cima a palavra e não dar erro. Vou até usar o mesmo nome
def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def pede_chute():
    chute = input ("Qual a letra?\n")
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute, letras_acertadas, palavra_chave):
      
    posição = 0
            
    for letra in palavra_chave:
        if (chute == letra):
            letras_acertadas[posição] = letra
        posição +=1
def ganhador():
    print ("*"*26,"Parabens!","*"*26)
    print ("Você venceeeeeeu, puta que pariu caralho porra!!!!")
def perdedor():
    print("~~","meu deus, que vergonha...", "~~")
    print("você perdeu...")
                    
if __name__ == "__main__":
    jogar_forca()
