from tkinter import *
from time import *

# Funciones
def actualizar():
    # Agregamos el formato de cadena con las siguientes opciones
    tiempo_cadena = strftime("%I:%M:%S %p")
    etiqueta_tiempo.config(text=tiempo_cadena)
    # Agregamos el formato de cadena con las siguientes opciones
    dia_cadena = strftime("%A")
    etiqueta_dia.config(text=dia_cadena)
    # Agregamos el formato de cadena con las siguientes opciones
    fecha_cadena = strftime("%B %D %Y")
    etiqueta_fecha.config(text=fecha_cadena)

    ventana.after(1000,actualizar)

ventana = Tk()

etiqueta_tiempo = Label(ventana,font=("Arial",50),fg="#00ff00",bg="black")
etiqueta_tiempo.pack()

etiqueta_dia = Label(ventana,font=("Arial",25))
etiqueta_dia.pack()

etiqueta_fecha = Label(ventana,font=("Arial",25))
etiqueta_fecha.pack()
# Llamamos a la función
actualizar()

ventana.mainloop()