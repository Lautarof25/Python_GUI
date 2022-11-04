from tkinter import *

def hacer_algo(event):     # Coorenada X   coordenada y
    print("Hiciste algo "+str(event.x)+" "+str(event.y))

ventana = Tk()
# Lista clicks
# <Button-1> click derecho
# <Button-2> click rueda
# <Button-3> click izquierdo
# <ButtonRelease> Mantener click
# <Enter> Mouse entra en la ventana
# <Leave> Mouse sale de la ventana
# <Motion> donde el mouse se mueve

ventana.bind("<Button-1>",hacer_algo)

ventana.mainloop()