from collections import deque

mi_cola = deque()
mi_cola.append(1)
mi_cola.append(2)
mi_cola.append(3)
print(mi_cola.popleft())  # Desencola el 1
