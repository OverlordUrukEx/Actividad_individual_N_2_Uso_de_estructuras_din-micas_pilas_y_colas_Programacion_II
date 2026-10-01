class _Nodo:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """Pila (LIFO) implementada con nodos."""

    def __init__(self):
        self._cima = None
        self._tamano = 0

    def apilar(self, dato) -> None:
        nodo = _Nodo(dato)
        nodo.siguiente = self._cima
        self._cima = nodo
        self._tamano += 1

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        dato = self._cima.dato
        self._cima = self._cima.siguiente
        self._tamano -= 1
        return dato

    def ver_cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._cima.dato

    def esta_vacia(self) -> bool:
        return self._cima is None

    def __len__(self) -> int:
        return self._tamano

    def __iter__(self):
        actual = self._cima
        while actual:
            yield actual.dato
            actual = actual.siguiente
