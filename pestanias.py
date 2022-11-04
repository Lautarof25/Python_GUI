from tkinter import *
from tkinter import ttk # Acceso a widgets

ventana = Tk()

# Ventana que maneja una colección de ventanas
notas = ttk.Notebook(ventana)

# Por cada ventana creamos un frame
pestania1 = Frame(notas) # Nuevo frame para la pestaña 1
pestania2 = Frame(notas) # Nuevo frame para la pestaña 2
# Agregamos las pestañas a las notas
notas.add(pestania1,text="Pestaña 1")
notas.add(pestania2,text="Pestaña 2")
# Insertamos las notas
notas.pack(expand=True, # Expand = Expande para llenar cualquier espacio
            fill="both" # fill = llena el espacio 'x' e 'y'
            )
# Creamos contenido para las pestañas
Label(pestania1,text="Hola, esta es la pestaña 1", width=50,height=50).pack()
Label(pestania2,text="Hola, esta es la pestaña 2", width=50,height=50).pack()

ventana.mainloop()