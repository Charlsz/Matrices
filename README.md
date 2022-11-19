# Matrices

Representar Z matrices dispersas con las listas enlazadas y de listas enlazadas volver a hacerla una matriz.

la idea para poder representar estas matrices es:
sigamos un ejemplo de una matriz 3v3

1 2 3
4 5 6      De esta matriz quedara una lista como la siquiente:
7 8 9      [ [1,2,3],[4,5,6],[7,8,9] ]

para leer las filas y columnas de esta matriz (NxM)

archivo.txt:     leer linea por linea y cada linea agregarla a un nodo
                ese nodo sera una lista (en este caso los valores de las filas)
                --> 1 2 3 --> addnode --> [1,2,3]
                --> 4 5 6 --> addnode --> [4,5,6]
                --> 7 8 9 --> addnode --> [7,8,9]

    Node va a contener estos valores como se representan ahi arriba

    [ Node1, Node2, Node3]
       ↕       ↕      ↕
    [1,2,3] [4,5,6] [7,8,9]