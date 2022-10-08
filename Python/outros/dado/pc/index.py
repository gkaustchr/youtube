# Imports
from random import choice, randint
from time import sleep
from tkinter import *
import pygame


# Funções
def btnGirar():
    global faceMaior
    if dadoEscolhido.get() == 1:
        faceMaior = 6
        girarDado()
    elif dadoEscolhido.get() == 2:
        faceMaior = 12
        girarDado()
    elif dadoEscolhido.get() == 3:
        faceMaior = 20
        girarDado()

def girarDado():
    numero = randint(faceMenor, faceMaior)
    pygame.mixer.music.load(f'{caminho}/{choice(audio)}')
    pygame.mixer.music.play()
    sleep(1.5)
    dado1.set(numero)


# Variaveis
faceMenor = 1
faceMaior = 6
caminho = 'Python/outros/dado/pc/audios'
audio = ['dice1.mp3', 'dice2.mp3', 'dice3.mp3', 'dice4.mp3', 'dice5.mp3', 'dice6.mp3' ]

pygame.init()
# Janela
dado = Tk()
dado.title('Dados')
dado.config(bg='white')
#dado.geometry('500x200')
dado.resizable(False, False)

dadoEscolhido = IntVar()
dado1 = StringVar()

face6 = Radiobutton(dado, text='6 Lados', value=1, font='Arial 14',bg='white', variable=dadoEscolhido)
face12 = Radiobutton(dado, text='12 Lados', value=2, font='Arial 14',bg='white', variable=dadoEscolhido)
face20 = Radiobutton(dado, text='20 Lados', value=3, font='Arial 14',bg='white', variable=dadoEscolhido)
face6.select()

face6.grid(row=0, column=0)
face12.grid(row=0, column=1)
face20.grid(row=0, column=2)

Button(dado, text='Girar', font='Arial 16', bg='red', fg='white', command=btnGirar).grid(columnspan=3)
lblDado1 = Label(dado, text='', font='Arial 30', textvariable=dado1, bg='#ffffff').grid(columnspan=3)

dado.mainloop()
#Programa
'''while True:
    print('Dado')
    menu = int(input('1 - 6 Lados \n2 - 12 Lados \n3 - 20 Lados\n R: '))
    if menu == 1:
        faceMaior = 6
        girarDado()
    elif menu == 2:
        faceMaior = 12
        girarDado()
    elif menu == 3:
        
        faceMaior = 20
        girarDado()
    else:
        break'''