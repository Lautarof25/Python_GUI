# Es usado para dibujar graficos, barras, imagenes en una ventana
from tkinter import *

ventana = Tk()

canvas = Canvas(ventana,height=500,width=500)
# Creamos formas
canvas.create_line(0,0,     # Inicio
                   500,500, # Final
                fill="blue", # color
                width=5 #ancho
                    )
canvas.create_line(0,500,500,0,fill="red",width=5)
canvas.create_rectangle(50,50,250,250, fill="purple")

puntos = [250,0,500,500,0,500]

canvas.create_polygon(puntos,fill="blue",outline="black",width=5)

canvas.create_arc(0,0,500,500,style=ARC,start=90,extent=180)

# canvas.pack()

# Creando una pokebola
pokebola = Canvas(ventana,height=500,width=500)
# Semi circulo Rojo
pokebola.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# Semi circulo blanco
pokebola.create_arc(0,0,500,500,fill="white",extent=180,width=10,start=180)
# Circulo centro 
pokebola.create_oval(190,190,310,310, fill="white",width=10)

pokebola.pack()
ventana.mainloop()