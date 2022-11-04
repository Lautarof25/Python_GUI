from tkinter import *
import time
from Pelota import *

ventana = Tk()

ANCHO = 500
ALTO = 500

canvas = Canvas(ventana,width=ANCHO,height=ALTO)
canvas.pack()

# Creamos las pelota usando la clase Pelota
pelota_voley = Pelota(canvas,0,0,100,1,1,"white")
pelota_tenis = Pelota(canvas,0,0,50,4,3,"yellow")
pelota_basket = Pelota(canvas,0,0,85,4,5,"orange")
pelota_futbol = Pelota(canvas,0,0,85,3,2,"red")

while True:
    pelota_voley.mover()
    pelota_tenis.mover()
    pelota_basket.mover()
    pelota_futbol.mover()
    ventana.update()
    time.sleep(0.01)

ventana.mainloop()