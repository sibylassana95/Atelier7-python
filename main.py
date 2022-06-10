from tkinter import *
  
def sel():
   selected = "Vous avez sélectionné : " + v.get()
   label.config(text = selected)

gui = Tk()
v = StringVar()
v.set("Python") # initialiser

r1 = Radiobutton(gui, text="Python", variable=v, value="Python", command=sel)
r1.pack(anchor = W)

r2 = Radiobutton(gui, text="Java", variable=v, value="Java", command=sel)
r2.pack(anchor = W)

r3 = Radiobutton(gui, text="PHP", variable=v, value="PHP", command=sel)
r3.pack(anchor = W)

label = Label(gui)
label.pack()
gui.mainloop()
