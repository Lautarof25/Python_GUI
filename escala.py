from tkinter import *

def enviar():
    print("La temperatura es:" + str(escala.get())+" grados centígrados  ")

ventana = Tk()

# Agregar imagenes
imagen_fuego = PhotoImage(file="fuego.png")
etiqueta_fuego = Label(image=imagen_fuego)
# Agregamos la imagen a la ventana
etiqueta_fuego.pack()

# Creamos la escala
escala = Scale(
    ventana,
    from_= 100,
    to=0,
    length=400,
    orient=VERTICAL, # Orientación
    font=('Arial',20),
    tickinterval=10, # Indicador numerico de la escala
    # showvalue=0, # Esconde el valor
    resolution=5, # Incremento del desplazamiento
    troughcolor="blue", # Color de la escala
    fg="#ff1c00",
    bg="#111111"
    )

escala.set(((escala["from"]-escala["to"])/2)+escala["to"])# Posicionarlo en el medio
escala.pack()



imagen_hielo = PhotoImage(file="hielo.png")
etiqueta_hielo = Label(image=imagen_hielo)
# Agregamos la imagen a la ventana
etiqueta_hielo.pack()

# Agregamos un botón para el texto
boton = Button(ventana,text="Enviar",command=enviar)
boton.pack()

ventana.mainloop()