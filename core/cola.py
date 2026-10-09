from collections import deque


class Cola:
    """Cola (FIFO) implementada sobre collections.deque.

    Se usa cuando los elementos deben procesarse en el mismo orden en que
    ingresan: se encola al final (``encolar``) y se desencola por el frente
    (``desencolar``). Aquí gestiona la agenda diaria y las urgencias por fecha.
    """

    def __init__(self):
        self._datos: deque = deque()

    def encolar(self, dato) -> None:
        self._datos.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos.popleft()

    def ver_frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos[0]

    def esta_vacia(self) -> bool:
        return not self._datos

    def __len__(self) -> int:
        return len(self._datos)

    def __iter__(self):
        return iter(self._datos)
