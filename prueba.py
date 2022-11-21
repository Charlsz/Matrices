from LinkedList import LinkedList
lista = LinkedList()
lista.AddNode()

lista2 = LinkedList()
lista2.AddNode2()


def recorrido(self):
    P = self.PTR
    while(P != None):
        print(P.data, end="->")
        P = P.next
    print("None")


"""
print("La primera matriz es: ")
print(lista)

print("La segunda matriz es: ")
print(lista2)
"""
