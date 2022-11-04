from tkinter import *

def enviar():
    entrada = texto.get("1.0",END)
    print(entrada)

ventana = Tk()

# Agregamos un text area
texto = Text(ventana,
            bg="lightyellow",
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")

# Agregamos el texto
texto.pack()

boton = Button(ventana,text="Enviar",command=enviar)
boton.pack()

ventana.mainloop()