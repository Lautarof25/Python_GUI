from tkinter import *

def abrir():
    print("El archivo ha sido abierto")
def guardar():
    print("El archivo ha sido guardado")
def copiar():
    print("El archivo ha sido copiado")
def cortar():
    print("El archivo ha sido cortado")
def pegar():
    print("El archivo ha sido pegado")

ventana = Tk()
# Agregamos un menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)
# Agregar iconos
abrir_imagen = PhotoImage(file="abrir.png")
guardar_imagen = PhotoImage(file="guardar.png")
salir_imagen = PhotoImage(file="salir.png")

# Agregamos el item "Archivo" al menu
menu_archivo = Menu(barra_menu,tearoff=0,font=("Arial",15))
barra_menu.add_cascade(label="Archivo",menu=menu_archivo)
# Agregamos items a la opción "Archivo"
menu_archivo.add_command(label="Abrir",command=abrir, image=abrir_imagen,compound="left")
menu_archivo.add_command(label="Guardar",command=guardar, image=guardar_imagen,compound="left")
# Agregar separador
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=quit, image=salir_imagen,compound="left")
# Agregamos el item "Editar" al menú
menu_editar = Menu(barra_menu,tearoff=0,font=("Arial",15))
barra_menu.add_cascade(label="Editar",menu=menu_editar)
# Agregamos items a la opción "Editar"
menu_editar.add_command(label="Copiar",command=copiar)
menu_editar.add_command(label="Cortar",command=cortar)
menu_editar.add_command(label="Pegar",command=pegar)

ventana.mainloop()