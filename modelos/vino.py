from modelos.entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def obtenerBodega(self):
        from servicios.vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self.bodega)

    def obtenerCepas(self):
        from servicios.vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self.cepas]

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.cepas,
            "partidas": self.partidas
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()
