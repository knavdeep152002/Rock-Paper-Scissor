from tkinter import *
import tkinter
from PIL import Image,ImageTk
from functools import partial

from . import RPStraining

root = Tk()
root.title("Rock Paper Scissor")
root.geometry("1000x600")
root.resizable(0, 0)

img = Image.open("Resources/Rocks.png")
rock = ImageTk.PhotoImage(img.resize((400,300),Image.ANTIALIAS))
img = Image.open("Resources/paper.png")
paper = ImageTk.PhotoImage(img.resize((400,300),Image.ANTIALIAS))
img = Image.open("Resources/scissor_left.png")
scissor_left = ImageTk.PhotoImage(img.resize((400,300),Image.ANTIALIAS))
img = Image.open("Resources/scissor_right.png")
scissor_right = ImageTk.PhotoImage(img.resize((400,300),Image.ANTIALIAS))


left = Frame(root,width=400,height=200)
left.pack(side=LEFT)

right = Frame(root,width=400,height=200)
right.pack(side=RIGHT)

label1 = Label(left,image=rock)
label1.image=rock
label1.pack()

label2 = Label(right,image=paper)
label2.image=paper
label2.pack()

def displayrock(side = "right"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(left,image=rock)
        label1.image=rock
        label1.pack()
    else:
        global label2
        label2.destroy()
        label2 = Label(right,image=rock)
        label2.image=rock
        label2.pack()

def displaypaper(side="left"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(left,image=paper)
        label1.image=paper
        label1.pack()
    else:
        global label2
        label2.destroy()
        label2 = Label(right,image=paper)
        label2.image=paper
        label2.pack()

def displayscissor(side="left"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(left,image=scissor_right)
        label1.image=scissor_right
        label1.pack()
    else:
        global label2
        label2.destroy()
        label2 = Label(right,image=scissor_left)
        label2.image=scissor_right
        label2.pack()

button1 = Button(text = "Rock",command=partial(displayrock,"left"))
button1.pack()
button2 = Button(text = "Paper",command= displaypaper)
button2.pack()
button3 = Button(text = "Scissor",command=displayscissor)
button3.pack()






root = mainloop()