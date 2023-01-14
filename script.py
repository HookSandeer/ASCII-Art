
#! By HookSander

from PIL import Image


def importPicture(path) :
    """
    Args:
        path (str): Chemin d'accès' de l'image

    Returns:
        PIL Image : L'image que nous allons convertir
    """
    return Image.open(path)


def resizePic(pic) :
    """
    Args:
        pic (PIL Image): L'image original

    Returns:
        PIL Image: La même mais redimensioné en 480p, 16/9
    """
    return pic.resize((854, 480))


def getPixel(pic) :
    print(pic.size)


    

if __name__ == '__main__' :
    
    picturePath = input("Entrer le chemin d'accès relatif de votre image\n=>")     #?# Récupération du chemin d'accès relatif 
    try :
        newPicture = resizePic(importPicture(picturePath))              #?# ###
    except :                                                            #?#   Prévention d'erreur
        print("Erreur durant le chargement de l'image")                 #?#  Arret si erreur
        exit()                                                          #?# ###
    
    