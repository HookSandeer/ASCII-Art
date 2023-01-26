#!/usr/bin/env python3
# Définition de l'interpreteur python pour system Linux
# Hookander

#### IMPORTS ####

# Import du module Pillow (pip install Pillow) qui va permettre la manipulation d'image
from PIL import Image, ImageDraw

# Import de Tkinter 
from tkinter import Tk

# Import du module tkinter pour le choix de l'image (boite de dalogue)
from tkinter.filedialog import askopenfilename

# Import du module tkinter pour l'enregistrement (seconde boite de dialogue)
from tkinter import filedialog
################


def chemin() :
    """Demande a l'utilisateur de séléctionner son image dans une boite de dialogue

    Returns:
        str : Chemin d'accès absolue de l'image
    """
    # Création de la fenêtre tkinter
    win = Tk()
    
    # Nom de la fenêtre
    win.title("Séléctionner l'image que vous souhaitez convertirs :")
    
    # Appelle du module de la boite de dialogue
    win.withdraw()
    
    # Renvoie du chemin d'accèes grâce au module de tkinter
    return askopenfilename()


def save(img) :
    """Enregistre l'image dans le dossier séléctionner via une boite de dialogue

    Args:
        img (Pillow Image): Image ASCII généré
    """
    # Cration de la fenêtre tkinter
    win = Tk()
    
    # Nom de la fenêtre 
    win.title("Choisissez le dossier d'enregistrement :")
    
    # Appelle du module de la boite de dialogue
    win.withdraw()
    
    # Récupère le chemin du dossier dans lequel le fichier image va être enregistré
    dossierSelect = filedialog.askdirectory()
    
    # Enregistrement dans le bon dossier, et défintion du nom de l'image
    img.save(dossierSelect+"/Ascii.png")


# Diviseur de la largeur et de la hauteur de l'image (Pour les proportions)
echelle = 0.09

# Largeur de chaque caractère en pixel, pour éviter que un M prenne plus de place qu'un i, décalant tout les lettres par exemple
largeurCara = 10
hauteurCara = 18


def caractere(num) :
    """En fonction du chiffre reçu en paramètre, renvoie le charactère correspondant
    au contraste.
    Args:
        num (int): Nuance de gris

    Returns:
        str : Caractère ascii corespondant a la nuance de gris
    """
    # Tout les caractère du codage ASCII
    asciiChar = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    
    # Convertion de la variable string en list, pour une manipulation plus simple
    listChar = list(asciiChar)
    
    # Renvoie du bon caractère de la liste, en fonction de la bonne nuance de gris (256 pour éviter le out of range)
    return listChar[num*len(listChar)//256]


# Importe l'image dans le programme
image = Image.open(chemin())

#!######
# police = ImageFont.truetype('/font/AdobeVFPrototype.ttf', 15) => Pour police personnalisé, mais occasione trop de problème
# lors de changement d'ordinateur (si la police n'est pas dispo, le programme s'arrete)
#!######


def resize(img, diviseur, larg, haut) :
    """Redimensionne l'image en fonction des paramètre pour qu'elle n'ai pas un nombre trop important de pixel
    afin que les caractère ascii soit encore visible, gros tas de lettre dans le cas contraire.

    Args:
        img (Pillow Image) : Image a redimensionner
        diviseur (float) : Echelle de redimension
        larg (int) : Largeur d'un caractère en pixel(pour conserver les proportions de l'image original)
        haut (int) : Hauteur d'un caractère en pixel (pour conserver les proportions de l'image original)

    Returns:
        Pillow Image: Même image, mais redimensionnée
    """
    # Définition des variable hauteur et largeur pour pourvoir garder les proportions
    largeur = img.width
    hauteur = img.height
    
    # Redimension, int pour ne pas avoir des float, et Image.NEAREST permet de paufiner les proportions pour éviter tout déséquilibre.
    img = img.resize((int(diviseur*largeur), int(diviseur*hauteur*(larg/haut))), Image.NEAREST)
    
    return img

# Redimensionne l'image grâce a la fonction resize
resizeImage = resize(image, echelle, largeurCara, hauteurCara)

# Redéfinie les nouvelles variables d'hauteur et de largeur suite a la redimension
largeur = resizeImage.width
hauteur = resizeImage.height

# Charge chaque pixel de l'image pour faire la convertion
pixel = resizeImage.load()

# Créer une nouvelle image dans laquelle les lettres vont être écrite au fur et a mesur. Les dimensions de celle ci sont dans le second paramètre
imageSortie = Image.new('RGB', (largeurCara * largeur, hauteurCara * hauteur), color = (0, 0, 0))
imageActuelle = ImageDraw.Draw(imageSortie)

# Double boucle (chaque ligne x le nombre de ligne (soit x et y))
for y in range(hauteur):
    for x in range(largeur):
        # Définition des valeurs de chaque piexel en RGB. Valeur comprise entre 0 et 255
        r, v, b = pixel[x, y]
        
        # Convertion en nuance de gris, pour choisir le charactère ascii correspondant
        c = int(r/3 + v/3 + b/3)
        
        # Remplacement des pixels par en nuance de gris, soit convertion en noir et blan
        pixel[x, y] = (c, c, c)
        
        # Ajout a limage du bon caractère, et coloration de la lettre en fonction de la couleur du pixel original (fill = (r, v, b).)
        # Définition de la coordonnée de placement en fonction du variant de boucle, et de la largeur et hauteur du caractère pour que ce soit 
        # espacé de façon égale.
        imageActuelle.text((x*largeurCara, y*hauteurCara), caractere(c), fill = (r, v, b))


# Enregistrement de l'image grâce a la fonction save.
save(imageSortie)