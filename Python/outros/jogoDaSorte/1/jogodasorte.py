# IMPORTS
from random import randint


# VARIÁVEIS 
chances = 0



# FUNÇÕES
def zerarValores():
    global chances
    chances = 0

def iniciarJogo(modo):
    zerarValores()
    if modo == 1:
        facil()
    elif modo == 2:
        medio()
    elif modo == 3:
        dificil()
    else:
        print('Desconhecido')

def facil():
    global chances
    menor = 0
    maior = 25
    segredo = randint(menor, maior)
    while True:
        chute = perguntar(menor, maior)
        chances += 1 #Tentativas
        if chute == segredo:
            print(' **** FIM DE PARTIDA **** ')
            print('    ** VOCÊ ACERTOU **   ')
            print(f'Tentativas: {chances}')
            break
        elif chute > segredo:
            print('MENOR')
        else:
            print('MAIOR')

def medio():
    global chances
    menor = 0
    maior = 100
    segredo = randint(menor, maior)
    while True:
        chute = perguntar(menor, maior)
        chances += 1 #Tentativas
        if chute == segredo:
            print(' **** FIM DE PARTIDA **** ')
            print('    ** VOCÊ ACERTOU **   ')
            print(f'Tentativas: {chances}')
            break
        elif chute > segredo:
            print('MENOR')
        else:
            print('MAIOR')

def dificil():
    global chances
    menor = 0
    maior = 100
    segredo = randint(menor, maior)
    while True:
        chute = perguntar(menor, maior)
        chances += 1 #Tentativas
        if chute == segredo:
            print(' **** FIM DE PARTIDA **** ')
            print('    ** VOCÊ ACERTOU **   ')
            print(f'Tentativas: {chances}')
            break

def perguntar(menor, maior):
    while True:
        chute = input(f'Digite um número entre {menor} e {maior}. \n R: ')
        if chute.isnumeric():
            chute = int(chute)
            if chute >= menor and chute <=maior:
                return chute
            else:
                print('Digite um NÚMERO dentro do intervalo indicado!')
        else:
            print('Digite um número válido')

# PROGRAMA 
print(' **** JOGO DA SORTE **** ')
while True:
    menu = input(' 1 - Fácil \n 2 - Médio \n 3 - Difícil \n 4 - Sair \n R: ')
    if menu.isnumeric():
        menu = int(menu)
        if menu > 0 and menu < 4:
            iniciarJogo(menu)
        else:
            print('JOGO FINALIZADO!')
            break
    else:
        print('Digite um NÚMERO!')