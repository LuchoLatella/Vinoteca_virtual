from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre

    def __eq__(self, other):
        return isinstance(other, EntidadVineria) and self.id == other.id

    @abstractmethod
    def convertirAJSON(self):
        pass
