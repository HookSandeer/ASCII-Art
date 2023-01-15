
#! By HookSander

from PIL import Image
import time

asciiChar =  " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrnxuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"


def importPicture(path) :
    return Image.open(path)


def resizePic(pic) :
    return pic.resize((256, 144))



def monochrome(pic) :
    return pic.convert("L")


def convertAscii(pic, char) :
    for y in range(144) :
        currentLine = ""
        for x in range(256) :
            pix = pic.getpixel((x, y))
            sym = pix * 67 // 255
            currentLine += char[sym] + " "
        print(currentLine)
        time.sleep(0.1)


if __name__ == '__main__' :
    
    picturePath = input("Entrer le chemin d'accès relatif de votre image\n=>")     #?# Récupération du chemin d'accès relatif 
    try :
        newPicture = resizePic(importPicture(picturePath))              #?# ###
    except :                                                            #?#   Prévention d'erreur
        print("Erreur durant le chargement de l'image")                 #?#  Arret si erreur
        exit()                                                          #?# ###
    
    monoPicture = monochrome(newPicture)
    convertAscii(monoPicture, asciiChar)