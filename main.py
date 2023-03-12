#!/usr/bin/python3
# By HookSander

#### IMPORTS ####
from PIL import Image as __Image                # Importe la gestion d'image Pillow sous la variable __Image
from PIL import ImageDraw                       # Importe l'outil de création d'image du module Pillow
from tkinter import *                           # Importe le module tkinter
from tkinter import filedialog                  # Pour l'enregistrement, sert a séléctionner le dossier
from tkinter.filedialog import askopenfilename  # Pour l'ouverture, sert a récupérer le chemin absolue de l'image
from tkinter import messagebox                  # Pour afficher les différents boites de dialogues
import sys                                      # Pour arreter le processus python


# Script

def quitter() :
    """Lors de l'appelle, ferme la fenêtre principal tkinter, et stop le processus python

    Returns:
        int : exit code 0
    """
    win.destroy()                               # Ferme la fenêtre Tkinter
    sys.exit()                                  # Ferme le processus python (evite que le programme tourne toujours en arrière plan)
    return 0


def main() :
    """FONCTION PRINCIPALE
    Importe dans le programme une image, la converti en ASCII Art, l'affiche et l'enregistre,
    suivant le choix de l'utilisateur.

    Returns:
        int : exit code 0
    """

    def chemin() :
        """Demande a l'utilisateur de séléctionner son image dans une boite de dialogue

        Returns:
            str : Chemin d'accès absolue de l'image
        """
        win = Tk()                                                      # Création de la fenêtre Tkinter temporaire
        title = "Séléctionner l'image que vous souhaitez convertir :"   # Variable nom de la fenêtre
        win.withdraw()                                                  # Module du gestionnaire de fichier (Module de kinter)
        return askopenfilename(filetypes=[('.JPG image files', '.jpg')], title=title)
        # Renvoie du chemin d'accèes grâce au module de tkinter, que jpg

    def savePath() :
        """Ouvre une fenêtre de dialogue
        L'utilisateur choisit le dossier et le nom d'enregistrement de l'image

        Returns:
            str : Chemin et nom de l'image a enregistrer
        """
        win = Tk()                                                      # Création de la fenêtre tkinter
        title = "Enregistrement :"                                      # Variable du nom de la fenêtre
        win.withdraw()                                                  # Appelle du module de la boite de dialogue
        return filedialog.asksaveasfilename(filetypes=[('Ascii Art Image', '*.png')], defaultextension='.png', title=title)
        # Récupère le chemin d'accès, et le nom que l'utilisateur a choisit pour son image
    

    def save(img) :
        """Enregistre l'image dans le dossier séléctionner via une boite de dialogue

        Args:
            img (Pillow Image): Image ASCII généré

        Returns:
            int : exit code 0
        """
        # Demande a l'utilisateur si il veut ouvrir l'image :
        userChoice = messagebox.askyesno(title="Ouverture ?", message="Souhaitez ouvrir l'image ?")
        if userChoice :                                                 # Ouvre l'image
            img.show()                                                  # la méthode .show du module pillow affiche l'image dans l'application par default
        # Demande a l'utilisateur si il souhaite enregistrer l'image :
        userChoice = messagebox.askyesno(title="Enregistrement ?", message="Souhaitez vous enregistrer l'image ?")
        if userChoice :
            img.save(savePath())                        # Enregistrement dans le bon dossier, et défintion du nom de l'image
            messagebox.showinfo(title="Info", message="Enregistrement terminée.")
            # Informe l'utilisateur que l'enregistrement est terminée.
        return 0


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
        listChar = list(asciiChar)                                      # Convertion de la variable string en list, pour une manipulation plus simple
        return listChar[num*len(listChar)//256]                         # Renvoie du bon caractère de la liste, en fonction de la bonne nuance de gris (256 pour éviter le out of range)


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


    # Importe l'image dans le programme
    try :                                                               # Evite l'erreur d'import dans le programme
        image = __Image.open(chemin())                                  # Import l'image dans le programme a l'aide de Pillow, chemin() renvoie le chemin d'accès absolu.
    except :                                                            # Si l'utilisateur clique sur "annuler", récupere l'erreur
        messagebox.showinfo(title='Info', message='Opération annulée')  # Informe que le programme a bien prit en compte l'annulation


    echelle = 0.2                                                       # Diviseur de la largeur et de la hauteur de l'image (Pour les proportions)
    # Largeur de chaque caractère en pixel, pour éviter que un M prenne plus de place qu'un i, décalant tout les lettres par exemple
    largeurCara = 8
    hauteurCara = 16
    resizeImage = resize(image, echelle, largeurCara, hauteurCara)

    # Redéfinie les nouvelles variables d'hauteur et de largeur suite a la redimension
    largeur = resizeImage.width
    hauteur = resizeImage.height

    # Charge chaque pixel de l'image pour faire la convertion
    pixel = resizeImage.load()

    # Créer une nouvelle image dans laquelle les lettres vont être écrite au fur et a mesur. Les dimensions de celle ci sont dans le second paramètre
    imageSortie = __Image.new('RGB', (largeurCara * largeur, hauteurCara * hauteur), color = (20, 20, 20))
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

    messagebox.showinfo(title='Info', message='Convertion terminé')


    # Enregistrement de l'image grâce a la fonction save.
    try :
        save(imageSortie)
    except :
        messagebox.showerror(title='Alerte', message='Enregistrement annulé.\nFermeture du programe')
        win.destroy()
        sys.exit()

    return 0




# Tkinter
# Création de la fenêtre :
win = Tk()
# Titre
win.title("Générateur ASCII Art")
# Dimmension
win.geometry('800x400')


# Titre
title = Label(win, text='Image en ASCII Art', font=('Arial', 30), fg='black')
title.pack()

# Instruction pour utilisateur
instruction1 = Label(win, text=' 1 - Lancer le programme, séléctionner une image au format *.jpg')
instruction1.place(x=50, y=100)

instruction2 = Label(win, text="2 - Une boite de dialogue s'ouvre, choisissez l'emplacement d'enregistrent" )
instruction2.place(x=50, y=150)

# Bouton de lancement du programme (lance la fonction main)
lancement = Button(win, text="Lancer le convertisseur", font=('Arial', 20), command=main)
lancement.place(x=250, y=250)

# Bouton pour quitter le programme (lance la fonction quitter)
quitter = Button(win, text='Quitter', font=('Arial', 10), command=quitter)
quitter.place(x=380, y=350)

# Affichage de la fenêtre principal
win.mainloop()


"""
INFORMATION :

Ce programme utilise 2 module python, tkinter et Pillow
Ils sont souvent déjà installés sur les machines, mais ce n'est pas tout le temps le cas pour Pillow
Pour installer pillow :
    - Ouvrir un terminal comme powershell ou cmd
    - tapez la commande pip install pillow

Chaque ligne est commenté pour la compréhension, et les fonctions ont leurs docstrings de renseignée,
avec les arguments et ce qu'elles renvoyent
Programme entièrement créer Par Michon Antonin pour un projet de NSI.
"""
