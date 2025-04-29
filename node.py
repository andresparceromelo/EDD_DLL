# Clase Base Lista Doblemente Enlazada (Modificada y Extendida)

import random

class node:
    __slots__ = ('value', '_prev', '_next')

    def __init__(self, value):
        self.value = value
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, Node):
        if Node is not None and not isinstance(Node, node):
            raise TypeError("next debe ser un objeto tipo node ó con el valor None")
        self._next = Node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, Node):
        if Node is not None and not isinstance(Node, node):
            raise TypeError("prev debe ser un objeto tipo node ó con el valor None")
        self._prev = Node

    def __str__(self):
        return f"({self.value['placa']}, {self.value['tipo']}, P{self.value['prioridad']})"
