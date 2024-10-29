# archivo: modelos/cepa.py
from .entidadvineria import EntidadVineria
from servicios.vinoteca import Vinoteca

class Cepa(EntidadVineria):
    def obtenerVinos(self):
        return [vino for vino in Vinoteca.obtenerVinos() if self.id in vino.cepas]

    def convertirAJSON(self):
        return {"id": self.id, "nombre": self.nombre, "vinos": [f"{vino.nombre} ({Vinoteca.buscarBodega(vino.bodega).nombre})" for vino in self.obtenerVinos()]}
