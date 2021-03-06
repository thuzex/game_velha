from player import Tabuleiro
from game import Game

t = Tabuleiro([ [0,0,0],[0,0,0],[0,0,0] ], 'Xadrez')
g = Game(1, 0)

print(t.modelo)
print(t.tipo)

def menu():
    while g.menu:
        g.menu = int(input("1. Jogar\n"+"0. Sair\n"))
        if g.menu:
            game()
        else:
            print("Que pena :(")

def game():
    while ganhou() == 0:
        print("\nJogador ", g.jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if t.modelo[linha-1][coluna-1] == 0:
            if(g.jogada%2+1)==1:
                t.modelo[linha-1][coluna-1]=1
            else:
                t.modelo[linha-1][coluna-1]=-1
        else:
            print("O lugar já está preenchido")
            g.jogada -=1

        if ganhou():
            print("Jogador ",g.jogada%2 + 1," ganhou apos ", g.jogada+1," rodadas")

        g.jogada +=1
    
def ganhou():
    for i in range(3):
        soma = t.modelo[i][0]+t.modelo[i][1]+t.modelo[i][2]

        if soma==3 or soma ==-3:
            return 1

    for i in range(3):
        soma = t.modelo[0][i]+t.modelo[1][i]+t.modelo[2][i]
        if soma==3 or soma ==-3:
            return 1

    diagonal1 = t.modelo[0][0]+t.modelo[1][1]+t.modelo[2][2]
    diagonal2 = t.modelo[0][2]+t.modelo[1][1]+t.modelo[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if t.modelo[i][j] == 0:
                print(" _ ", end=' ')
            elif t.modelo[i][j] == 1:
                print(" X ", end=' ')
            elif t.modelo[i][j] == -1:
                print(" O ", end=' ')

        print()


def resultados_jogo(lista):

    t = Tabuleiro('[ [0,0,0],[0,0,0],[0,0,0] ]', 'Xadrez')

menu()