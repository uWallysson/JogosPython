import forca
import adivinhacao

def escolhe_jogo():
    print("=================================")
    print("=========Escolha seu jogo========")
    print("=================================")

    print("(1) Forca (2)Adivinhação")

    jogo = int(input("Qual o seu jogo? "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()