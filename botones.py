from tkinter import *
# Funciones fuera de la ventana 

# Funcion click
def click():
    global contador_clicks
    contador_clicks +=1
    print(contador_clicks)

# creando contado
# Contar la cantidad de veces que cliqueamos
contador_clicks = 0

ventana = Tk()

# Agregar foto
foto = PhotoImage(file='1.png')

# Configuracion del boton
boton = Button(ventana,
              text="Cliquear",
              command=click, # Agregar la función
              font=("Comic Sans",30),
              fg="#00ee00",
              bg="black",
              activeforeground="#00ff00", # Agregar fondo letra
              activebackground="black", # Agregar fondo al cliquear
              state=ACTIVE, # Estado activado
              image=foto,
              compound='bottom')
# Agregar boton a la ventana
boton.pack()

ventana.mainloop()