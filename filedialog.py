from tkinter import *
from tkinter import filedialog

def abrir_archivo():
    # Abrir archivo
    ruta_archivo = filedialog.askopenfilename()
    # Abrir la carpeta por default
    ruta_archivo = filedialog.askopenfilename(
        initialdir="c:\\Users\\user\\desktop\\carpeta",
        title="Abrir archivo",
        filetypes=(("Archivo de texto","*.txt"),("Todos los archivos","*.*")))
    # Leer archivo
    archivo = open(ruta_archivo,"r")
    # Imprimir contenido
    print(archivo.read())
    archivo.close()

ventana = Tk()

boton = Button(text="Abrir",command=abrir_archivo)
boton.pack()

ventana.mainloop()