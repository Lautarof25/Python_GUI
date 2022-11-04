from tkinter import *
ventana = Tk()

# Agregar una foto
foto = PhotoImage(file='1.png')
# Label: un area que guarda texto o imágenes
# configuraciones
etiqueta = Label(ventana,
                 text="Hola mundo",
                 font=("Arial",40,'bold'),
                 fg="green",
                 bg="red",
                 relief=RAISED,
                 bd=10,
                 padx=20,
                 pady=20,
                 image=foto,
                 compound='top'
                 )

# Situar la etiqueta en la ventana
etiqueta.pack() # centrar etiqueta
# etiqueta.place(x=0,y=0) # situar etiqueta segun coordenadas

ventana.mainloop()