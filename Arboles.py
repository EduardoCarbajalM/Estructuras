class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Ejemplo de un árbol binario
raiz = NodoArbol(1)
raiz.izquierda = NodoArbol(2)
raiz.derecha = NodoArbol(3)
