from tkinter import *
root = Tk()
root.title("Rock Paper Scissor")
root.geometry("500x500")

canvas = Canvas(root)      
canvas.pack(fill=BOTH, expand=1)      
img = PhotoImage(file="Hand.png")      
canvas.create_image(255,255, image=img)      
root.after(20000, lambda: canvas.delete(img))

rock = Button(text="Rock")
rock.pack(side=LEFT, padx=(20, 0), pady=(0, 20))

paper = Button(text="Paper")
paper.pack(side=LEFT, padx=(20, 20), pady=(0, 20))

scissor = Button(text = "Scissor")
scissor.pack(side=LEFT, padx=(0, 20), pady=(0, 20))

root = mainloop()