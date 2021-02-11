from tkinter import *
import tkinter
from PIL import Image,ImageTk
from functools import partial

# from . import RPStraining

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

win_count = tie_count = lose_count = 0

def call_rock():
    global expression,win_count,tie_count,lose_count
    displayrock()
    n = system_rand()
    if n==2:
        expression = "Win"
        win_count+=1
    elif n==1:
        expression = "Lose"
        lose_count+=1
    else:
        expression = "Tie"
        tie_count+=1 
    display.set(expression)
    count1.set("Win : "+str(win_count))
    count2.set("Tie : "+str(tie_count))
    count3.set("Lose : "+str(lose_count))

def call_paper():
    global expression,win_count,tie_count,lose_count
    displaypaper()
    n = system_rand()
    if n==0:
        expression = "Win"
        win_count+=1
    elif n==2:
        expression = "Lose"
        lose_count+=1
    else:
        expression = "Tie"
        tie_count+=1
    display.set(expression)
    count1.set("Win : "+str(win_count))
    count2.set("Tie : "+str(tie_count))
    count3.set("Lose : "+str(lose_count))

def call_scissor():
    global expression,win_count,tie_count,lose_count
    displayscissor()
    n = system_rand()
    if n==1:
        expression = "Win"
        win_count+=1
    elif n==0:
        expression = "Lose"
        lose_count+=1
    else:
        expression = "Tie"
        tie_count+=1
    display.set(expression)
    count1.set("Win : "+str(win_count))
    count2.set("Tie : "+str(tie_count))
    count3.set("Lose : "+str(lose_count))

def displayrock(side = "left"):
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

import random
def system_rand():
    n = random.randint(0,2)
    if n==0:
        displayrock(side="right")
    elif n==1:
        displaypaper(side="right")
    else:
        displayscissor(side="right")
    return n

button1 = Button(text = "Rock",command=call_rock)
button1.pack()
button2 = Button(text = "Paper",command= call_paper)
button2.pack()
button3 = Button(text = "Scissor",command=call_scissor)
button3.pack()

frame = Frame(root,highlightbackground="Black",width=24,height=50,highlightcolor="Black")
frame.pack()
expression=""
display = StringVar()
display.set(expression)
entry_field = Label(frame,textvariable=display,width=24,bd=0,bg="Grey",fg="White",font=("arial",18,"bold"))
entry_field.pack(ipady=10)

frame_cal = Frame(root,highlightbackground="Black",width=24,height=50,highlightcolor="Black")
frame_cal.pack()

count1 ,count2, count3 = StringVar(), StringVar(), StringVar()
count1.set("Win : 0")
count2.set("Tie : 0")
count3.set("Lose : 0")
Label_1 = Label(frame,textvariable=count1,width=24,bd=0,bg="black",fg="White",font=("arial",18,"bold"))
Label_2 = Label(frame,textvariable=count2,width=24,bd=0,bg="black",fg="White",font=("arial",18,"bold"))
Label_3 = Label(frame,textvariable=count3,width=24,bd=0,bg="black",fg="White",font=("arial",18,"bold"))
Label_1.pack()
Label_2.pack()
Label_3.pack()





root = mainloop()