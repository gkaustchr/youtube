# IMPORTS
from random import choice


# VARIAVEIS
palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']
chutes = []
exibirAcertos = []
palavraJaSaiu = []
palavraSecreta = ''
tentativas = 5

# FUNÇÕES
def jogar():
    global tentativas
    iniciaValores()
    while True:
        chute = input('Digite uma letra R: ').strip().upper() # A, X
        if encontrarLetra(chute):
            exibePalavraJogo()
        else:
            if not verificarRepetiuChute(chute):
                tentativas -= 1
                chutes.append(chute)
            exibePalavraJogo()
            print(f'INFO \n - Letra {chute} não encontrada \n - {chutes} \n - Restam {tentativas} tentativas')

        if tentativas <= 0:
            derrota()
            break

        if verificaVitoria():
            vitoria()
            break

def encontrarLetra(chute):
    temLetra = False
    if len(chute) > 1: # PIA = 3 letras
        if chute == palavraSecreta: # CASA = PIA
            temLetra = True
            for posicao, letra in enumerate(palavraSecreta):
                exibirAcertos[posicao] = letra
    else:
        for posicao, letra in enumerate(palavraSecreta): # 2, S
            if chute == letra:
                exibirAcertos[posicao] = chute # _ _ S _  
                temLetra = True
    return temLetra

def iniciaValores():
    global palavraSecreta, exibirAcertos, tentativas, chutes, palavraJaSaiu
    while True:
        palavraSecreta = choice(palavras).upper()
        if not palavraSecreta in palavraJaSaiu:
            palavraJaSaiu.append(palavraSecreta)
            break
        if len(palavraJaSaiu) == len(palavras):
            palavraJaSaiu = []

    exibirAcertos = []
    chutes = []
    tentativas = 5

    for espaco in palavraSecreta: # CASA 
        exibirAcertos.append('_') # exibirAcertos ['_', '_', '_', '_']

    exibePalavraJogo()

def verificaVitoria():
    if '_' in exibirAcertos: # _ _ _ _ -> C _ S _ -> C A S A 
        return False
    return True

def exibePalavraJogo():
    # ['_', '_']
    for espaco in exibirAcertos:
        print(espaco, end='  ') # -> _  A  _  A
    print(' ')

def verificarRepetiuChute(chute):
    if chute in chutes: # T = ['T', 'C']
        return True
    return False

def vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def derrota():
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")  

# INICIO DO PROGRAMA
print('Jogo da Forca')
while True:
    menu = input('1 - Jogar \n2 - Sair \n R: ')
    if menu.isnumeric():
        if int(menu) == 1:
            jogar()
        else:
            print('Finalizando jogo')
            break
    else:
        print('Insira um valor válido')