
#! By HookSander

from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def picToAscii() :
    listAscii = " .,:;*+?%$#@"
    finalText = ""
    win = Tk()
    win.withdraw()
    picturePath = askopenfilename()
    pictureFile = Image.open(picturePath)
    pictureResize = pictureFile.resize((160, 128))
    pictureMono = pictureResize.convert("L")
    
    for y in range(128) :
        for x in range(160) :
            pixel = pictureMono.getpixel((x, y))
            sym = (pixel*len(listAscii)//255)-1
            finalText += listAscii[sym] + "  "
        finalText += "\n"
    
    return finalText


def textToImage(text) :
    img = Image.new("RGB", (1920, 1080), (0, 0, 0))
    image = ImageDraw.Draw(img)
    fontType = ImageFont.truetype('DejaVuSerif.ttf', 3)
    image.text((50, 50), text, (255, 255, 255), font=fontType)
    img.save("AsciiArt.jpg")
     