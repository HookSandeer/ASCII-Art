#!/usr/bin/env python3
# By HookSander

#### IMPORTS ####
from tkinter import *


win = Tk()
win.title("Générateur ASCII Art")
win.geometry('1600x800')

title = Label(win, text='Image en ASCII Art', font=('Arial', 30), fg='black')
title.pack()

text = Label(win, text='Image séléctionnée :', font=('Arial', 20), fg='black')
text.place(x=50, y=200)

picturePath = Text(win, font=('Arial', 15), width=70, height=1, state='disabled')
picturePath.place(x=350, y=200)

changeButton = Button(win, text='Modifier')
changeButton.place(x=1200, y=200)

convertButton = Button(win, text='Convertir', font=('Arial'), fg='black')
convertButton.place(x=750, y=400)

textExit = Label(win, text='Image rendu : ', font=('Arial', 20), fg='black')
textExit.place(x=50, y=600)

imageName = Text(win, font=('Arial', 15), width=70, height=1, state='disabled')
imageName.place(x=350, y=600)

saveButton = Button(win, text='Enregistrer sous')
saveButton.place(x=1200, y=600)

win.mainloop()