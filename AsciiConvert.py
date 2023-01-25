#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

def chemin() :
    win = Tk()
    win.withdraw()
    return askopenfilename()


def save(img) :
    win = Tk()
    win.withdraw()
    dossierSelect = filedialog.askdirectory()
    img.save(dossierSelect+"/Ascii.png")


echelle = 0.09

largeurCara = 10
hauteurCara = 18


def caractere(num) :
    asciiChar = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    listChar = list(asciiChar)
    return listChar[num*len(listChar)//256]


image = Image.open(chemin())

police = ImageFont.truetype('DejaVuSansMono.ttf', 15)

largeur, hauteur = image.size
image = image.resize((int(echelle*largeur), int(echelle*hauteur*(largeurCara/hauteurCara))), Image.NEAREST)
largeur, hauteur = image.size
pixel = image.load()

imageSortie = Image.new('RGB', (largeurCara * largeur, hauteurCara * hauteur), color = (0, 0, 0))
imageActuelle = ImageDraw.Draw(imageSortie)

for y in range(hauteur):
    for x in range(largeur):
        r, v, b = pixel[x, y]
        h = int(r/3 + v/3 + b/3)
        pixel[x, y] = (h, h, h)
        imageActuelle.text((x*largeurCara, y*hauteurCara), caractere(h), font = police, fill = (r, v, b))


save(imageSortie)