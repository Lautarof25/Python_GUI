from tkinter import *

# Funciones
# Función enviar
def enviar():
    usuario = entrada.get()
    print("Hola "+ usuario)
    # Deshabilitar después de enviar
    entrada.config(state=DISABLED)

# Función Borrar
def borrar():
    entrada.delete(0,END)

# Función suprimir
def borrar():
    entrada.delete(len(entrada.get())-1,END)

ventana = Tk()

# Crear y configurar entrada de texto
entrada = Entry(ventana,
                font=("Arial",50),
                fg="#00ff00",
                bg="black",
                show="*"### ocultar caracter con *
                )

# situar la entrada
entrada.pack(side=LEFT)

# Texto por default
entrada.insert(0,"BobSponja")

# Crear boton enviar
boton_enviar = Button(ventana,text="Enviar", command=enviar)
# situar boton
boton_enviar.pack(side=RIGHT)

# Crear boton borrar
boton_borrar = Button(ventana,text="Borrar", command=borrar)
# situar boton
boton_borrar.pack(side=RIGHT)

# Crear boton suprimir
boton_suprimir = Button(ventana,text="Suprimir", command=borrar)
# situar boton
boton_suprimir.pack(side=RIGHT)

ventana.mainloop()