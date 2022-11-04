from tkinter import *

def mover_arriba(event):
    canvas.move(mi_imagen,0,-10)
def mover_abajo(event):
    canvas.move(mi_imagen,0,10)
def mover_izquierda(event):
    canvas.move(mi_imagen,-10,0)
def mover_derecha(event):
    canvas.move(mi_imagen,10,0)

ventana = Tk()

ventana.bind("<w>",mover_arriba)
ventana.bind("<s>",mover_abajo)
ventana.bind("<a>",mover_izquierda)
ventana.bind("<d>",mover_derecha)

ventana.bind("<Up>",mover_arriba)
ventana.bind("<Down>",mover_abajo)
ventana.bind("<Left>",mover_izquierda)
ventana.bind("<Right>",mover_derecha)

canvas = Canvas(ventana,width=500,height=500)
canvas.pack()

imagen_foto = PhotoImage(file="auto.png")
mi_imagen = canvas.create_image(0,0,image=imagen_foto,anchor=NW)

ventana.mainloop()