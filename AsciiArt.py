
# By HookSander

#### IMPORTS ####
from PIL import Image as __Image
# Problème de conflit entre tkinter et Pillow
# Une variable Image est commune au deux. 
# Il faut donc changer le nom de la variale grâce au 'as' lors de l'import
from PIL import ImageDraw
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


# Script

def programme() :
    def chemin() :
        """Demande a l'utilisateur de séléctionner son image dans une boite de dialogue

        Returns:
            str : Chemin d'accès absolue de l'image
        """
        # Création de la fenêtre tkinter
        win = Tk()
        
        # Nom de la fenêtre
        title = "Séléctionner l'image que vous souhaitez convertir :"
        
        # Appelle du module de la boite de dialogue
        win.withdraw()
        
        # Renvoie du chemin d'accèes grâce au module de tkinter, que jpg
        return askopenfilename(filetypes=[('.JPG image files', '.jpg')], title=title)


    def save(img) :
        """Enregistre l'image dans le dossier séléctionner via une boite de dialogue

        Args:
            img (Pillow Image): Image ASCII généré
        """
        # Cration de la fenêtre tkinter
        win = Tk()
        
        # Nom de la fenêtre 
        title = "Choisissez le dossier d'enregistrement :"
        
        # Appelle du module de la boite de dialogue
        win.withdraw()
        
        # Récupère le chemin du dossier dans lequel le fichier image va être enregistré
        dossierSelect = filedialog.askdirectory(title=title)
        
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
    image = __Image.open(chemin())

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
        img = img.resize((int(diviseur*largeur), int(diviseur*hauteur*(larg/haut))), __Image.NEAREST)
        
        return img

    # Redimensionne l'image grâce a la fonction resize
    resizeImage = resize(image, echelle, largeurCara, hauteurCara)

    # Redéfinie les nouvelles variables d'hauteur et de largeur suite a la redimension
    largeur = resizeImage.width
    hauteur = resizeImage.height

    # Charge chaque pixel de l'image pour faire la convertion
    pixel = resizeImage.load()

    # Créer une nouvelle image dans laquelle les lettres vont être écrite au fur et a mesur. Les dimensions de celle ci sont dans le second paramètre
    imageSortie = __Image.new('RGB', (largeurCara * largeur, hauteurCara * hauteur), color = (0, 0, 0))
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
    win.destroy()
    exit()

# Tkinter
win = Tk()
win.title("Générateur ASCII Art")
win.geometry('800x400')

title = Label(win, text='Image en ASCII Art', font=('Arial', 30), fg='black')
title.pack()

instruction1 = Label(win, text=' 1 - Lancer le programme, séléctionner une image au format *.jpg')
instruction1.place(x=50, y=100)

instruction2 = Label(win, text="2 - Une boite de dialogue s'ouvre, choisissez l'emplacement d'enregistrent" )
instruction2.place(x=50, y=150)

lancement = Button(win, text="Lancer le convertisseur", font=('Arial', 20), command=programme)
lancement.place(x=250, y=250)

win.mainloop()