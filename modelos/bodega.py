from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from servicios.vinoteca import Vinoteca
        return [vino for vino in Vinoteca.obtenerVinos() if vino.bodega == self.id]

    def obtenerCepas(self):
        cepas = set()
        for vino in self.obtenerVinos():
            cepas.update(vino.cepas)
        return list(cepas)

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.obtenerCepas(),
            "vinos": [vino.nombre for vino in self.obtenerVinos()]
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()
