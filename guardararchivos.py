from tkinter import *
from tkinter import filedialog

def guardar_archivo():
    archivo = filedialog.asksaveasfile(
                    initialdir="C:\\Users\\user\\desktop\\carpeta",
                    defaultextension=".txt",
                    filetypes=[("Archivo de texto",".txt"),
                    ("Archivo HTML",".html"),
                    ("Todos los archivos",".*")])
    # Prevenir error al salvar el archivo
    if archivo is None:
        return
    archivo_texto = str(texto.get(1.0,END))# Convertimos todo a texto
    # Ingresar texto al archivo desde consola
    archivo.write(archivo_texto)
    archivo.close()

ventana = Tk()

boton = Button(text="Guardar", command=guardar_archivo)
boton.pack()

texto = Text(ventana)
texto.pack()


ventana.mainloop()