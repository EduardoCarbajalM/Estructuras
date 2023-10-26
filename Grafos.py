grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Obtener los vecinos del nodo 'B'
print(grafo['B'])  # Devuelve ['A', 'C', 'D']
