from tkinter import *

def hacer_algo(event):
    print("Presionaste "+ event.keysym)
    etiqueta.config(text=event.keysym)


ventana = Tk()
# Lista de teclas
# <Return>
# <Down>
# <UP>
# <q> ...

ventana.bind("<Key>",hacer_algo)

etiqueta = Label(ventana,font=("Arial",15))
etiqueta.pack()


ventana.mainloop()