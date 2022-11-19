from re import *
from Nodo import Nodo

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self):
        file = open('Matriz21x21.txt')
        while(True):
            linea = file.readline
            ln = linea.split(' ')
            P = Nodo()
            if (self.PTR == None):
                self.PTR = P
                self.ULT = P 
            else:
                self.ULT.next = P
                self.ULT = P             

    def Recorrido(self):
        P = self.PTR
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta