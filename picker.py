from tkinter import *
from tkinter import colorchooser

def click():
    # Usamos una función para elegir el color
    color = colorchooser.askcolor()
    
    # Creamos una variable para extraer el color hexa
    color_hexa = color[1]
    # Agregamos el color a la ventana
    ventana.config(bg=color_hexa)

ventana = Tk()

ventana.geometry("420x420")

boton = Button(text="Click acá", command=click)
boton.pack()

ventana.mainloop()
