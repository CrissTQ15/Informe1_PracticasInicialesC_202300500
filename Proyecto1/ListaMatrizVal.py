from NodoMatrizContenido import NodoMatrizContenido

class ListaMatrizVal:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.size = 0


    def insertar(self, valor, posx, posy):
        nuevaMatriz= NodoMatrizContenido(valor, posx, posy)
        if self.cabeza is None:
            self.cabeza = nuevaMatriz
            self.ultimo = nuevaMatriz
            self.size += 1
        else:
            self.ultimo.next = nuevaMatriz
            self.ultimo = nuevaMatriz
            self.size += 1

    def imprimirMatriz(self):
        auxiliar: NodoMatrizContenido = self.cabeza
        for envio in range(self.size):
            print(f"Valor:{auxiliar.valor} Posicion X:{auxiliar.posx} Posicion Y:{auxiliar.posy}") #imprime el valor cada elemento de la matriz
            auxiiliar = auxiliar.next
