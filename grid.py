# Organizar widgets en un contenedor como una tabla
from tkinter import *

ventana = Tk()
# Agregar un título
etiqueta_titulo = Label(ventana,text="Ingrese su información", font=("Arial",12)).grid(row=0,column=0,columnspan=2)

# Agregamos una etiqueta junto a su entrada de texto
etiqueta_nombre = Label(ventana,text="Nombre: ",width=20).grid(row=1,column=0)
entrada_nombre = Entry(ventana).grid(row=1,column=1)
# Agregamos una etiqueta junto a su entrada de texto
etiqueta_apellido = Label(ventana,text="Apellido: ",width=20).grid(row=2,column=0)
entrada_apellido = Entry(ventana).grid(row=2,column=1)
# Agregamos una etiqueta junto a su entrada de texto
etiqueta_email = Label(ventana,text="Email: ",width=20).grid(row=3,column=0)
entrada_email = Entry(ventana).grid(row=3,column=1)
# Agregamos un botón
boton_enviar = Button(ventana, text="Enviar").grid(row=4,column=0,columnspan=2)

ventana.mainloop()

