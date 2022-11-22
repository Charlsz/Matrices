from re import *
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.numeros = LinkedList()

    
    def __repr__(self):
        return str(self.data)

class NodoFila:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def addNodeFila(self, data):
        P = NodoFila(data)
        if (self.PTR == None): 
            self.PTR = P
            self.ULT = P
        else:    
            self.ULT.next = P
            self.ULT = P

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
            for x in ln:
                try:
                    P.numeros.addNodeFila(int(x))
                except ValueError:
                    pass
            if not linea:
                break
        file.close()
        
    def AddNode2(self):
        """agrega la fila de la matriz a un nodo"""
        file = open('Matriz21p21.txt')
        while(True):
            """leer linea por linea y agregar esos valores al nodo"""
            linea = file.readline()
            ln2 = linea.split(" ")
            P = Nodo(",".join(ln2))
            if (self.PTR == None):
                self.PTR = P
                self.ULT = P 
            else:
                self.ULT.next = P
                self.ULT = P
            for x in ln2:
                try:
                    P.numeros.addNodeFila(int(x))
                except ValueError:
                    pass
            if not linea:
                break
        file.close()
    
    def suma(self,lista2):
        P = self.PTR
        Q = lista2.PTR
        while P != None and Q != None:
            P2 = P.numeros.PTR
            Q2 = Q.numeros.PTR
            print("Aqui estamos:",P2)
            l = []
            while P2 != None and Q2 != None:
                
                if(P2.data!= None and Q2.data!=None):
                    #print("Aqui estamos:",P2.data,"y Q es",Q2.data)
                    P2.data = int(P2.data) + int(Q2.data)
                    l.append(P2.data)
                P2 = P2.next
                Q2 = Q2.next
            print(l)
            P = P.next
            Q = Q.next

    def resta(self,lista2):
        P = self.PTR
        Q = lista2.PTR
        while P != None or Q != None:
            P2 = P.numeros.PTR
            Q2 = Q.numeros.PTR
            while P2 != None or Q2 != None:
                if(P2.data!= None and Q2.data!=None):
                    P2.data = int(P2.data) - int(Q2.data)
                P2 = P2.next
                Q2 = Q2.next
            P = P.next
            Q = Q.next

    def __repr__(self) -> str:
        P = self.PTR
        texto = ""
        while P != None:
            texto = texto + str(P.data) + " -> "
            P = P.next
        return texto

