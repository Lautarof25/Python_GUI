# Creamos una clase nueva llamada pelota.py

class Pelota:

    def __init__(self,canvas, x,y,diametro, xVelocidad, yVelocidad,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diametro,diametro,fill=color)
        self.xVelocidad = xVelocidad
        self.yVelocidad = yVelocidad

    def mover(self):
        coordenadas = self.canvas.coords(self.image)
        # Si los canvas tocan el borde, rebotan
        if(coordenadas[2]>=(self.canvas.winfo_width()) or coordenadas[0]<0):
            self.xVelocidad = -self.xVelocidad
        if(coordenadas[3]>=(self.canvas.winfo_height()) or coordenadas[1]<0):
            self.yVelocidad = -self.yVelocidad

        # Hacemos que se muevan los canvas
        self.canvas.move(self.image,self.xVelocidad,self.yVelocidad)