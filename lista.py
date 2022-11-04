from tkinter import *

# Función enviar
# Botón Enviar
def enviar():
    # Selección multiple
    comidas = []
    # Iteramos sobre cada selección
    for i in lista_items.curselection():
        comidas.insert(i,lista_items.get(i))
    print("Su orden es: ")
    # Iteramos sobre cada uno de los items selecionados
    for i in comidas:
        print(i)

# Función agregar
def agregar():
    lista_items.insert(lista_items.size()# Esto nos da la posición actual
                    ,caja_texto.get())# Esto inserta lo que escribamos en la caja
    lista_items.config(height=lista_items.size())# Corregimos el alto de la lista

# Función borrar
def borrar():
    for i in reversed(lista_items.curselection()):# Invierte la selección 
        lista_items.delete(i)
    lista_items.config(height=lista_items.size())# Corregimos el alto de la lista

ventana = Tk()

# Agregamos la lista
lista_items = Listbox(
                ventana,
                bg="#f7ffde",
                font=("Arial",15),
                width=12,
                selectmode=MULTIPLE
                )
# Insertamos a la lista
lista_items.pack()
# Insertamos los items
lista_items.insert(1,"Pizza")
lista_items.insert(2,"Hamburguesa")
lista_items.insert(3,"Pancho")
lista_items.insert(4,"Empanada")
lista_items.insert(5,"Milanesa")
# Ajustar la linea al alto de los items
lista_items.config(height=lista_items.size())
 
# Entrada de texto
caja_texto = Entry(ventana)
caja_texto.pack()

# Creamos un botón de enviar
boton_enviar = Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack()
# Creamos un boton de agregar
boton_agregar = Button(ventana,text="Agregar",command=agregar)
boton_agregar.pack()
# Creamos un boton de borrar
boton_borrar = Button(ventana,text="Borrar",command=borrar)
boton_borrar.pack()

ventana.mainloop()