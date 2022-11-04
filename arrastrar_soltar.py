from tkinter import *
# Función arrastre
def arrastrar_inicio(event):
    # etiqueta.startX = event.x
    # etiqueta.startY = event.y
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def arrastrar_movimiento(event):
    # x = etiqueta.winfo_x() - etiqueta.startX + event.x
    # y = etiqueta.winfo_y() - etiqueta.startY + event.y
    # etiqueta.place(x=x,y=y)
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

ventana = Tk()

# Creamos una etiqueta
etiqueta = Label(ventana,bg="red",width=10,height=5)
etiqueta.place(x=0,y=0)
# Creamos otra etiqueta
etiqueta2 = Label(ventana,bg="blue",width=10,height=5)
# Le ponemos una coordenada 00
# Le ponemos una coordenada 100,100
etiqueta2.place(x=100,y=100)
# Creamos una función para iniciar el arrastre
etiqueta.bind("<Button-1>",arrastrar_inicio)
# Creamos una función para mover la caja
etiqueta.bind("<B1-Motion>",arrastrar_movimiento)

etiqueta2.bind("<Button-1>",arrastrar_inicio)
# Creamos una función para mover la caja
etiqueta2.bind("<B1-Motion>",arrastrar_movimiento)


ventana.mainloop()