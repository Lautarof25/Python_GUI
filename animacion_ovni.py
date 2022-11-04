from tkinter import *
import time

# Creamos constantes
ANCHO = 500
ALTO = 500
# Creamos las velocidades
x_velocidad = 3
y_velocidad = 2

ventana = Tk()

canvas = Canvas(ventana,width=ANCHO, height=ALTO)
canvas.pack()

# Creamos una foto
fondo = PhotoImage(file="space.png")
# le asignamos un id unico
mi_fondo = canvas.create_image(0,0,image=fondo)

# Creamos una foto
ovni = PhotoImage(file="ovni.png")
# le asignamos un id unico
mi_imagen = canvas.create_image(0,0,image=ovni,anchor=NW)

ancho_imagen = ovni.width() 
alto_imagen = ovni.height()

while True:
    # Las coordenadas de la imagen
    coordenadas = canvas.coords(mi_imagen)
    print(coordenadas)
    # Esto hace que la imagen vaya de un lado al otro en el eje x
    if(coordenadas[0] >= (ANCHO - ancho_imagen) or coordenadas[0]< 0):
        x_velocidad =  -x_velocidad
    # Esto hace que la imagen vaya de un lado al otro en el eje y
    if(coordenadas[1] >= (ALTO - alto_imagen) or coordenadas[1]< 0):
        y_velocidad =  -y_velocidad
    # generamos la funciòn de movimiento
    canvas.move(mi_imagen,x_velocidad,y_velocidad)
    # Actualizamos la ventana
    ventana.update()
    # Damos un retraso de 0.01 segundos
    time.sleep(0.01)

ventana.mainloop()