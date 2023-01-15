
#! By HookSander


from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import time

asciiChar =  " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrnxuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"

def locatePicture() :
    win = Tk()
    win.withdraw()
    path = askopenfilename()
    return path

def importPicture(path) :
    return Image.open(path)


def resizePic(pic) :
    return pic.resize((256, 144))



def monochrome(pic) :
    return pic.convert("L")


asciiChar =  " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrnxuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"
#asciiChar = " .^~:/[o%O@"
#asciiChar = " .:/o0@"

def convertAscii(pic, char) :
    for y in range(144) :
        currentLine = ""
        for x in range(256) :
            pix = pic.getpixel((x, y))
            sym = (pix*len(char)//255)-1
            currentLine += char[sym] + " "
        print(currentLine)

if __name__ == '__main__' :
    picturePath = locatePicture()
    try :
        newPicture = resizePic(importPicture(picturePath))              #?# ###
    except :                                                            #?#   Prévention d'erreur
        print("Erreur durant le chargement de l'image")                 #?#  Arret si erreur
        exit()                                                          #?# ###
    
    monoPicture = monochrome(newPicture)
    convertAscii(monoPicture, asciiChar)