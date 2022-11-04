from tkinter import *

def mover_arriba(event):
    etiqueta.place(x=etiqueta.winfo_x(),y=etiqueta.winfo_y()-5)
def mover_abajo(event):
    etiqueta.place(x=etiqueta.winfo_x(),y=etiqueta.winfo_y()+5)
def mover_izquierda(event):
    etiqueta.place(x=etiqueta.winfo_x()-5,y=etiqueta.winfo_y())
def mover_derecha(event):
    etiqueta.place(x=etiqueta.winfo_x()+5,y=etiqueta.winfo_y())

ventana = Tk()

ventana.bind("<w>",mover_arriba)
ventana.bind("<s>",mover_abajo)
ventana.bind("<a>",mover_izquierda)
ventana.bind("<d>",mover_derecha)
ventana.bind("<Up>",mover_arriba)
ventana.bind("<Down>",mover_abajo)
ventana.bind("<Left>",mover_izquierda)
ventana.bind("<Right>",mover_derecha)

mi_imagen = PhotoImage(file="auto.png")

etiqueta = Label(ventana, image=mi_imagen)
etiqueta.place(x=0,y=0)

ventana.mainloop()