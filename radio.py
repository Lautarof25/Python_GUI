from tkinter import *
# Creamos una lista de comidas
comidas = ["Pizza","Hamburguesa","Pancho"]

# Función pedido
def pedido():
    if(x.get()==0):
        print("Ordenaste una pizza")
    elif (x.get()== 1):
        print("Ordenaste una hamgurguesa")
    elif (x.get()== 2):
        print("Ordenaste un pancho")
    else:
        print("Error")

ventana = Tk()

# Agregamos nuestra imagenes
imagen_pizza = PhotoImage(file="pizza.png")
imagen_burger = PhotoImage(file="hamburguesa.png")
imagen_hot = PhotoImage(file="hot-dog.png")
# Creamos una lista de imágenes
imagenes_comidas = [imagen_pizza,imagen_burger,imagen_hot]


# Declaramos una variable 
x = IntVar()

# Iteramos sobre cada elemento de la lista
for index in range(len(comidas)):
    boton_radio = Radiobutton(
                    ventana,
                    text=comidas[index], # Agregamos texto al radio
                    variable=x,# Agrupa los radios juntos si tiene la misma variable
                    value=index,# Asigna a cada radio un valor diferente
                    padx=25, # Agrega padding en el eje x
                    font=("Impact",15), # Agregamos una fuente y tamaño
                    image=imagenes_comidas[index], #Agrega una imagen al radio
                    compound="left", # Alinea las imagenes a la izquierda
                    indicator=0, # Elimina el círculo
                    width= 250, # Agrega ancho a los radios
                    command=pedido # Agregamos la función
                    )

    boton_radio.pack(anchor=W)# Alineacion a la izquierda "Western"

ventana.mainloop()