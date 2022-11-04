from tkinter import *

ventana = Tk()

# Agrupar botones 
frame = Frame(ventana,bg="pink",bd=5,relief=SUNKEN)
frame.pack(side=BOTTOM)

Button(frame, text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame, text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="D",font=("Consolas",25),width=3).pack(side=LEFT)

ventana.mainloop()