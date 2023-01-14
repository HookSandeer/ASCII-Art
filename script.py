
#! By HookSander

from PIL import Image
import time

def importPicture(path) :
    return Image.open(path)

def resizePic(pic) :
    return pic.resize((854, 480))


    

if __name__ == '__main__' :
    picturePath = input("Enter your Picture emplacement path\n=>")
    try :
        newPicture = resizePic(importPicture(picturePath))
    except :
        print("Error in your picture path, please try again.")
        exit()
    