from tkinter import *

# Función mostrar
def mostrar():
    if(x.get()== 1): # Verificarmos intVar()
        print("De acuerdo")
    else:
        print("No estoy de acuerdo")

ventana = Tk()

# Crear variable para verificar 
x = IntVar()
# Puede ser con valor booleano o String
# x = BooleanVar()
# x = StringVar()

# Agregar imagen
imagen = PhotoImage(file="2.png")

# Crear botón de verificación
boton_check = Checkbutton(
            ventana,
            text="¿Estas de acuerdo?",
            variable=x, # Agreagmos nuestra variable
            onvalue=1, # valor 1 # Podemos usar valores booleanos o string - True o "Si"
            offvalue=0, # Valor 0 # False o "No"
            command=mostrar, # función mostrar
            font=("Arial", 20),
            fg="#00ff00",
            bg="black",
            activeforeground="#00ff00",
            activebackground="black",
            padx=25,
            pady=10,
            image=imagen,
            compound="left"
                )
# Agregar botón
boton_check.pack()
ventana.mainloop()