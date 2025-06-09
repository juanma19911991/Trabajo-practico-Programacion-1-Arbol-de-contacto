import time

# Clase para representar un contacto
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

# Nodo del árbol binario
class Nodo:
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None

# Árbol binario de búsqueda para contactos
class ArbolContactos:
    def __init__(self):
        self.raiz = None

    def insertar(self, contacto):
        def _insertar(nodo, contacto):
            if not nodo:
                return Nodo(contacto)
            if contacto.nombre < nodo.contacto.nombre:
                nodo.izquierda = _insertar(nodo.izquierda, contacto)
            else:
                nodo.derecha = _insertar(nodo.derecha, contacto)
            return nodo

        self.raiz = _insertar(self.raiz, contacto)

    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if not nodo:
                return None
            if nombre == nodo.contacto.nombre:
                return nodo.contacto
            elif nombre < nodo.contacto.nombre:
                return _buscar(nodo.izquierda, nombre)
            else:
                return _buscar(nodo.derecha, nombre)

        return _buscar(self.raiz, nombre)

    def inorden(self):
        resultados = []

        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultados.append(str(nodo.contacto))
                _inorden(nodo.derecha)

        _inorden(self.raiz)
        return resultados

# --- Uso del árbol ---

# Lista de nombres para insertar
nombres = ["Carlos", "Ana", "Diego", "Beatriz", "Eduardo", "Fabián", "Gabriela", "Héctor"]

# Crear árbol
arbol = ArbolContactos()

# Medir tiempo de inserción
inicio_insercion = time.time()
for nombre in nombres:
    telefono = f"+54 9 11 0000-{nombres.index(nombre):04}"
    arbol.insertar(Contacto(nombre, telefono))
fin_insercion = time.time()

# Medir tiempo de búsqueda
inicio_busqueda = time.time()
resultado = arbol.buscar("Gabriela")
fin_busqueda = time.time()

# Mostrar resultados
print("Contactos ordenados (inorden):")
for contacto in arbol.inorden():
    print(contacto)

print("\nResultado de búsqueda:")
print(resultado)

print(f"\nTiempo total de inserción: {fin_insercion - inicio_insercion:.6f} segundos")
print(f"Tiempo de búsqueda: {fin_busqueda - inicio_busqueda:.6f} segundos")
