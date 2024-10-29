# archivo: modelos/bodega.py
from modelos.entidadvineria import EntidadVineria
from servicios.vinoteca import Vinoteca

class Bodega(EntidadVineria):
    def obtenerVinos(self):
        return [vino for vino in Vinoteca.obtenerVinos() if vino.bodega == self.id]

    def obtenerCepas(self):
        cepas = set()
        for vino in self.obtenerVinos():
            cepas.update(vino.cepas)
        return list(cepas)

    def convertirAJSON(self):
        return {"id": self.id, "nombre": self.nombre, "cepas": self.obtenerCepas(), "vinos": [vino.nombre for vino in self.obtenerVinos()]}
