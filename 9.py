# -*- coding: iso-8859-15 -*-

#Ex.1 - Desenhando circulos com cores e tamanhos aleatórios em posições aleatórias na tela
from Tkinter import *
import time
import random

def desenhaCirculos():
    while True:
        R = random.randint(100, 255)
        G = random.randint(100, 255)
        B = random.randint(100, 255)

        diametroDoCirculo = random.randint(1, 101)

        x1 = random.randint(1, 601)
        y1 = random.randint(1, 601)
        x2 = x1 + diametroDoCirculo
        y2 = y1 + diametroDoCirculo

        mapa.create_oval(x1, y1, x2, y2, fill='#%02x%02x%02x' % (R,G,B))

        mapa.update()
        time.sleep(0.01)
    
root = Tk()
root.title('desenhaCirculos')

options = Frame(root, bg = 'black')
options.pack(fill = 'x', expand = True)

botao1 = Button(options, text = 'Comecar a Desenhar!', command = desenhaCirculos)
botao1.pack(side = 'left', fill = 'x', expand = True)

mapa = Canvas(root, width = 600, height = 400)
mapa.pack()

mainloop()

####################################################

#Ex.1 - Fazendo um circulo de cor aleatória e tamanho fixo se mover horizontalmente na tela
from Tkinter import *
import time
import random

def desenhaCirculos():
    diametroDoCirculo = 25
    variacao = 10

    x1 = 0
    y1 = 200
    y2 = y1 + diametroDoCirculo

    R = random.randint(100, 255)
    G = random.randint(100, 255)
    B = random.randint(100, 255)

    while True:
        if (x1 + variacao) >= 600:
            variacao *= -1
            
        if (x1 + variacao) <= 0:
            variacao *= -1

        x1 = x1 + variacao
        x2 = x1 + diametroDoCirculo

        mapa.create_oval(x1, y1, x2, y2, fill='#%02x%02x%02x' % (R,G,B), tag = "circulo")
        mapa.update()
        mapa.delete('circulo')
        time.sleep(0.02)
    
root = Tk()
root.title('desenhaCirculos')

options = Frame(root, bg = 'black')
options.pack(fill = 'x', expand = True)

botao1 = Button(options, text = 'Comecar a Desenhar!', command = desenhaCirculos)
botao1.pack(side = 'left', fill = 'x', expand = True)

mapa = Canvas(root, width = 600, height = 400)
mapa.pack()

mainloop()