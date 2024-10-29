# archivo: modelos/vino.py
from .entidadvineria import EntidadVineria
from servicios.vinoteca import Vinoteca

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def obtenerBodega(self):
        return Vinoteca.buscarBodega(self.bodega)

    def obtenerCepas(self):
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self.cepas]

    def convertirAJSON(self):
        return {"id": self.id, "nombre": self.nombre, "bodega": self.obtenerBodega().nombre, "cepas": self.obtenerCepas(), "partidas": self.partidas}
