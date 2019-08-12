from random import randint as rand
#JOGO FODA DA VELHA
tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
playerStatus = 0
playerSymbol = 0
iaStatus = 0
'''
if(PlayerStatus == 1):
        play = int(input("Em qual casa pretende jogar? ")
'''

#refazer de forma a evitar a sobreposição de casas a partir de validPlay()
def iaFodaProgramadaAsPressas():
    if(iaStatus==1):
        play = rand(0,2)
        play = play + (rand(0,2)*10)
        return(play)

#isso tá certo e num tem q mudar
def caraCoroa():
    start = rand(0, 1)
    if(start == 1):
        playerStatus = 1

#tá certo tbm
def crossBall():
    start = rand(0, 1)
    if(start == 1):
        playerSymbol = 1

#refazer de forma a verificar o estado de cara jogador
def validPlay(play):
    while True:
        if(play<10):
           tabuleiro[0][play] = 1
        elif(play<20):
           tabuleiro[1][play-10] = 1
        elif(play<30):
           tabuleiro[2][play-20] = 1
        else:
            print("O número colocado não corresponde a uma casa válida")
                
        
def Jogo():
    print("JOGO DA VELHA MUITO FODA")
    print("APERTE ENTER PARA JOGAR")

    crossBall()
    caraCoroa()                   
     '''
        Faltam algumas coisas:
            >Implementar a 'velha': Quando não há mais possibilidade de jogada
            >Implementar uma IA que não seja uma fracassada fudidda do caralho
            >Fazer validPlay retornar as posições ocupadas para uma lista
            >Produzir um mapa gráfico para guiar o usuário
