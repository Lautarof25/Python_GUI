from tkinter import *

def crear_ventana():
    nueva_ventana = Tk(), # Nueva ventana independiente
    Toplevel() # Nueva ventana en parte superior
    vieja_ventana.destroy() # Cierra la vieja ventana

vieja_ventana = Tk()

Button(vieja_ventana,text="Crear una nueva ventana",padx=20,pady=20,command=crear_ventana).pack()

vieja_ventana.mainloop()