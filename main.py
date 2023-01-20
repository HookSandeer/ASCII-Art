
#! By HookSander

from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def chemin() :
    win = Tk()
    win.withdraw()
    return askopenfilename()



police = ImageFont.truetype('Lucon.ttf', 15)

def caractere(num) :
    asciiChar = " -oW@"
    listChar = list(asciiChar)
    return listChar[num*len(listChar)//256]


echelleRedimension = 0.1
largeurCaractere = 10
hauteurCaractere = 18
photo = Image.open(chemin())
largeur, hauteur = photo.size
image = photo.resize((int(echelleRedimension*largeur), int(echelleRedimension*hauteur)), Image.NEAREST)
largeur, hauteur = image.size
imageActuelle = image.load()

imageSortie = Image.new('RGB', (largeurCaractere*largeur, hauteurCaractere*hauteur), color = (0, 0, 0))
imageAjoutTexte = ImageDraw.Draw(imageSortie)


for y in range(largeur) :
    for x in range(hauteur) :
        r, v, b = imageActuelle[x, y]
        a = int(r/3 + v/3 + b/3)
        imageActuelle[x, y] = (a, a, a)
        imageAjoutTexte.text((x*largeurCaractere, y*hauteurCaractere), caractere(a), font = police, fill = (r, v, b))
    
imageSortie.save('Ascii.png')