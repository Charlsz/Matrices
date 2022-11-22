class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.numeros = LinkedList()
    def __repr__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None
    def addNode(self, data):
        P = Nodo(data)
        if (self.PTR == None): 
            self.PTR = P
            self.ULT = P
        else:    
            self.ULT.next = P
            self.ULT = P
    def addNodeFila(self, data):
        P = NodoFila(data)
        if (self.PTR == None): 
            self.PTR = P
            self.ULT = P
        else:    
            self.ULT.next = P
            self.ULT = P
    def __repr__(self) -> str:
        P = self.PTR
        texto = ""
        while P != None:
            texto = texto + str(P.data) + " -> "
            P = P.next
        return texto
    def suma(self,lista2):
        P = self.PTR
        Q = lista2.PTR
        while P != None or Q != None:
            P2 = P.numeros.PTR
            Q2 = Q.numeros.PTR
            while P2 != None or Q2 != None:
                P2.data = int(P2.data) + int(Q2.data)
                P2 = P2.next
                Q2 = Q2.next
            P = P.next
            Q = Q.next

class NodoFila:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

CarlosEsGay = LinkedList()
CarlosEsGay.addNode("1")
CarlosEsGay.PTR.numeros.addNodeFila("21")
CarlosEsGay.PTR.numeros.addNodeFila("22")
CarlosEsGay.PTR.numeros.addNodeFila("23")
CarlosEsGay.addNode("2") 
CarlosEsGay.PTR.next.numeros.addNodeFila("24")
CarlosEsGay.PTR.next.numeros.addNodeFila("25")
CarlosEsGay.PTR.next.numeros.addNodeFila("26")

CarlosEsMuyGay = LinkedList()
CarlosEsMuyGay.addNode("1")
CarlosEsMuyGay.PTR.numeros.addNodeFila("22")
CarlosEsMuyGay.PTR.numeros.addNodeFila("23")
CarlosEsMuyGay.PTR.numeros.addNodeFila("24")
CarlosEsMuyGay.addNode("2")
CarlosEsMuyGay.PTR.next.numeros.addNodeFila("25")
CarlosEsMuyGay.PTR.next.numeros.addNodeFila("26")
CarlosEsMuyGay.PTR.next.numeros.addNodeFila("27")

CarlosEsGay.suma(CarlosEsMuyGay)

print(CarlosEsGay.PTR.numeros)
print(CarlosEsGay.PTR.next.numeros)


count = 1
a = input("Fila: ")
b = input("Columna: ")
P = CarlosEsGay.PTR.numeros.PTR
while P != None:
    if count == int(b):
        print("El dato es: ", P.data)
        print("[", a, "]", "[", b, "]")
        break
    count += 1
    P = P.next
