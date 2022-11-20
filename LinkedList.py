from re import *
from Nodo import Nodo

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self):
        """agrega la fila de la matriz a un nodo"""
        file = open('Matriz21x21.txt')
        while(True):
            """leer linea por linea y agregar esos valores al nodo"""
            linea = file.readline()
            ln = linea.split(" ")
            P = Nodo(",".join(ln))
            if (self.PTR == None):
                self.PTR = P
                self.ULT = P 
            else:
                self.ULT.next = P
                self.ULT = P

            if not linea:
                break
        file.close()
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "Final Matriz"
        return respuesta
