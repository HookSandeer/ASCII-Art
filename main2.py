
#! By HookSander

from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


win = Tk()
win.withdraw()
path = askopenfilename()


def whichChar(color) :
    asciiChar = ' -"|@'
    listAscii = list(asciiChar)
    char = color*len(listAscii)//256
    return listAscii[char]

resize = 0.1

try :
    pic = Image.open(path)
except :
    print("Erreur lors du chargement de l'image")
width, height = pic.size
pic = pic.resize((int(resize*width), int(resize*height)))
width, height = pic.size
eachPix = pic.load()

file = open("Output.txt", "w") 
text = ""
for y in range(height) :
    for x in range(width) :
        r, g, b = eachPix[x, y]
        average = int(r/3 + g/3 + b/3)
        eachPix[x, y] = (average, average, average)
        file.write(whichChar(average))
        text += whichChar(average)
    file.write("\n")
    text += "\n"