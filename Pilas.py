class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

# Ejemplo de uso de una pila
mi_pila = Pila()
mi_pila.apilar(1)
mi_pila.apilar(2)
mi_pila.apilar(3)
print(mi_pila.desapilar())  # Desapila el 3
