# graphical user interface
# Widget = Elementos de gui, botones, cajas de texto, etiquetas.
# Windows = Sirve como contenedor para sostener o contener widgets

from tkinter import *

# Crear ventana
ventana = Tk()

# Dimensionar ventana
ventana.geometry("420x420")
# Poner título a la ventana
ventana.title("Usando GUI")
# Poner Icono a la ventana
icono = PhotoImage(file='1.png')
ventana.iconphoto(True,icono)
# Configuraciones de ventana - fondo
ventana.config(background="#ccfcff")
# Abrir ventana
ventana.mainloop()