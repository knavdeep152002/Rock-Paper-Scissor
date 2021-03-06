from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from PIL import Image,ImageTk
from functools import partial

import RPStraining as Rp



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


label1 = Label(root,image=rock)
label1.image=rock
label1.place(x=20,y=100)
label1.configure(highlightthickness=0, borderwidth=0)

label2 = Label(root,image=paper)
label2.image=paper
label2.place(x=580,y=100)
label2.configure(highlightthickness=0, borderwidth=0)

win_count = tie_count = lose_count = 0

def call_rock():
    global expression,win_count,tie_count,lose_count
    displayrock()
    n = system_rand(0)
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
    button1["bg"] = "black"
    button1["fg"] = "white"
    button2["bg"] = "white"
    button2["fg"] = "black"
    button3["bg"] = "white"
    button3["fg"] = "black"

def call_paper():
    global expression,win_count,tie_count,lose_count
    displaypaper()
    n = system_rand(1)
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
    button2["bg"] = "black"
    button2["fg"] = "white"
    button1["bg"] = "white"
    button1["fg"] = "black"
    button3["bg"] = "white"
    button3["fg"] = "black"
    
def call_scissor():
    global expression,win_count,tie_count,lose_count
    displayscissor()
    n = system_rand(2)
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
    button3["bg"] = "black"
    button3["fg"] = "white"
    button2["bg"] = "white"
    button2["fg"] = "black"
    button1["bg"] = "white"
    button1["fg"] = "black"
    
def displayrock(side = "left"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(root,image=rock)
        label1.image=rock
        label1.place(x=20,y=100)
        label1.configure(highlightthickness=0, borderwidth=0)
    else:
        global label2
        label2.destroy()
        label2 = Label(root,image=rock)
        label2.image=rock
        label2.place(x=580,y=100)
        label2.configure(highlightthickness=0, borderwidth=0)
        

def displaypaper(side="left"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(root,image=paper)
        label1.image=paper
        label1.place(x=20,y=100)
        label1.configure(highlightthickness=0, borderwidth=0)

    else:
        global label2
        label2.destroy()
        label2 = Label(root,image=paper)
        label2.image=paper
        label2.place(x=580,y=100)
        label2.configure(highlightthickness=0, borderwidth=0)


def displayscissor(side="left"):
    if side=="left":
        global label1
        label1.destroy()
        label1 = Label(root,image=scissor_right)
        label1.image=scissor_right
        label1.place(x=20,y=100)
        label1.configure(highlightthickness=0, borderwidth=0)

    else:
        global label2
        label2.destroy()
        label2 = Label(root,image=scissor_left)
        label2.image=scissor_right
        label2.place(x=580,y=100)
        label2.configure(highlightthickness=0, borderwidth=0)




button1 = Button(root,text = "Rock",command=call_rock,width = 8,height=2,highlightcolor="black",cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE)
button1.place(x=20,y=410)
button2 = Button(root,text = "Paper",command= call_paper,width = 8,height=2,cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE)
button2.place(x=180,y=410)
button3 = Button(root,text = "Scissor",command=call_scissor,width = 8,height=2,cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE)
button3.place(x=329,y=410)


button4 = Button(root,text = "Rock",width = 8,height=2,highlightcolor="black",cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE, state=DISABLED)
button4.place(x=600,y=410)
button5 = Button(root,text = "Paper",width = 8,height=2,cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE, state=DISABLED)
button5.place(x=740,y=410)
button6 = Button(root,text = "Scissor",width = 8,height=2,cursor="hand2",bg="white", borderwidth=1.5, relief=RIDGE, state=DISABLED)
button6.place(x=869,y=410)

import random
def system_rand(n):
    sys = Rp.myfunction(n)
    if sys==0:
        displayrock(side="right")
        button4.configure(fg = "white", bg="black")
        button5.configure(fg="black", bg="white")
        button6.configure(fg="black", bg="white")
    elif sys==1:
        displaypaper(side="right")
        button5.configure(fg = "white", bg="black")
        button4.configure(fg="black", bg="white")
        button6.configure(fg="black", bg="white")
    else:
        displayscissor(side="right")
        button6.configure(fg = "white", bg="black")
        button5.configure(fg="black", bg="white")
        button4.configure(fg="black", bg="white")
    return sys

expression="Start"
display = StringVar()
display.set(expression)
entry_field = Label(root,textvariable=display,width=24,bd=0,bg="white",fg="black",font=("Courier",38,"bold"))
entry_field.place(x=420,y=500)

count1 ,count2, count3 = StringVar(), StringVar(), StringVar()
count1.set("Win : 0")
count2.set("Tie : 0")
count3.set("Lose : 0")
Label_1 = Label(root,textvariable=count1,width=24,bd=0,bg="black",fg="White",font=("arial",28,"bold"))
Label_2 = Label(root,textvariable=count2,width=24,bd=0,bg="black",fg="White",font=("arial",28,"bold"))
Label_3 = Label(root,textvariable=count3,width=24,bd=0,bg="black",fg="White",font=("arial",28,"bold"))
Label_1.pack()
Label_2.pack()
Label_3.pack()




root['bg']="white"

root = mainloop()