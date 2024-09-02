from  NodoMatriz import NodoMatriz 
# #Clase que se encarga de almacenar las matrices en una lista
# esta es una lista circular

class ListaMatrices:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.size = 0 #tamaño de la lista

    #metodo que se encarga de insertar una matriz en la lista
    def agregarMatriz(self, nombre, n, m, listaValores):
        nuevaMatriz = NodoMatriz(nombre, n, m) #crea un nuevo nodo de matriz con el nombre y las dimensiones
        nuevaMatriz.valor = listaValores #le asigna la lista de valores a la matriz, apuntando
        if self.cabeza is None: #si la lista de matrices esta vacia
            self.cabeza = nuevaMatriz 
            self.ultimo = nuevaMatriz
            self.ultimo.next = self.cabeza
            self.size += 1
        else:
            self.ultimo.next = nuevaMatriz #si la lista no esta vacia, se le asigna el nuevo nodo al ultimo nodo
            self.ultimo = nuevaMatriz #se actualiza el ultimo nodo
            self.ultimo.next = self.cabeza
            self.size += 1
    
    def imprimirMatrices(self):
        
        if self.cabeza is None:
            print("No hay matrices")
            
        
        auxiliar:NodoMatriz = self.cabeza


        while True:
            #extra el atributo de la matriz como nombre, filas y columnas

            print(f"----Matriz: {auxiliar.matriz.nombre}, filas: {auxiliar.matriz.n}, columnas: {auxiliar.matriz.m}")
            aux = auxiliar.valor.cabeza #revisa la lista de valores de la matriz
            for i in range(aux.valor.size):
                print(f"Valor: {aux.valor.valor} en posicion X: {aux.valor.posx} Y: {aux.valor.posy}")
                #ver cuantos valores tiene la matriz
                aux = aux.next
            if auxiliar.next ==self.cabeza:
                break
            auxiliar = auxiliar.next
    