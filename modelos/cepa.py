from modelos.entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from servicios.vinoteca import Vinoteca
        return [vino for vino in Vinoteca.obtenerVinos() if self.id in vino.cepas]

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "vinos": [f"{vino.nombre} ({vino.obtenerBodega().obtenerNombre()})" for vino in self.obtenerVinos()]
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()
