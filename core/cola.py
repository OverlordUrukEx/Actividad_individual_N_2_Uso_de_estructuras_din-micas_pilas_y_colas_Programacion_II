class _Nodo:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """Cola (FIFO) implementada con nodos."""

    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, dato) -> None:
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self._frente = nodo
        else:
            self._final.siguiente = nodo
        self._final = nodo
        self._tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._tamano -= 1
        return dato

    def ver_frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._frente.dato

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._tamano

    def __iter__(self):
        actual = self._frente
        while actual:
            yield actual.dato
            actual = actual.siguiente
