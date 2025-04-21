
#  generador lineal congruencial
#  Xsub(n-1) =  (a * Xsub(n) + c) mod m            i=0,1,2....
#  El valor inicial X0 es la semilla;
#  a es el multiplicador constante
#  c es el incremento
#  m es el modulo


import time

class randomGenerate:
    def __init__(self, semilla=None):
        if semilla is None:
            semilla = int(time.time())
        self.semilla=semilla
        self.a = 5254
        self.c = 412
        self.m = 1098

    def siguiente(self):
        self.semilla = (self.a * self.semilla + self.c) % self.m
        return self.semilla

    