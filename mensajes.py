from tkinter import *
from tkinter import messagebox

def click():
    # # Info
    # messagebox.showinfo(title="Titulo de ventana",
    #                     message='Eres una persona')
    # # Advertencia
    # messagebox.showwarning(title="Advertencia",
    #                     message='Es una advertencia')
    # # Error
    # messagebox.showerror(title="Error",
    #                     message='Es un error')

    #  Pregunta Aceptar - Cancelar
    if messagebox.askokcancel(title="Haz ok para cancelar",message="hacer algo"):
        print("Hiciste algo")
    else:
        print("Cancelaste algo")

    #  Pregunta reintentar o cancelar
    if messagebox.askretrycancel(title="haz ok para cancelar",
                                    message="Quieres reintentar"):
        print("Reintentaste algo")
    else:
        print("Cancelaste algo")
    #  Pregunta Si o no
    if messagebox.askyesno(title="responde si o no",
                         message="Te gusta la pizza?"):
        print("Me gusta la pizza")
    else:
        print("Por qué no te gusta la pizza?")
    #  Pregunta
    respuesta = messagebox.askquestion(title="responde pregunta",
                            message="Te gusta la tarta?")
    if(respuesta == "yes"):
        print("Me gusta la tarta")
    else:
        print("No me gusta la tarta")

    # Pregunta
    respuesta = messagebox.askyesnocancel(title="si no cancelar",
                                message="Te gusta programar?",icon="info")
    if(respuesta==True):
        print("Te gusta codear")
    elif(respuesta==False):
        print("No te gusta codear")
    else:
        print("No respondiste")
    # Cerrar ventana después de un tiempo
    ventana.after(3000,lambda:ventana.destroy())


ventana = Tk()

# Creamos botón
boton = Button(ventana, command=click, text="Haz click")
# Insertamos botón
boton.pack()

ventana.mainloop()