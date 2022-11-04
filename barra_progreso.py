from tkinter import *
from tkinter.ttk import *
import time

# Funcion
def empezar():
    GB = 10
    descarga = 0
    velocidad = 1
    while(descarga < GB):
        time.sleep(0.05)
        barra["value"]+=(velocidad/GB)*100
        descarga += velocidad
        porcentaje.set(str(int((descarga/GB)*100))+"%")
        texto.set(str(descarga)+"/"+str(GB)+" Gb completados")
        ventana.update_idletasks()

ventana = Tk()
# Creamos variables de tipo String
porcentaje = StringVar()
texto = StringVar()
# Agregamos la barra de progreso
barra = Progressbar(ventana,orient=HORIZONTAL,length=300)
barra.pack(pady=10)

# Agreagamos las etiquetas
etiqueta_porcentaje = Label(ventana,textvariable=porcentaje).pack()
etiqueta_texto = Label(ventana,textvariable=texto).pack()

boton = Button(ventana,text="Descargar",command=empezar).pack()

ventana.mainloop()
