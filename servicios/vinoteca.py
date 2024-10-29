import json

class Vinoteca:
    archivoDeDatos = "data/vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.archivoDeDatos, 'r') as archivo:
            return json.load(archivo)

    @classmethod
    def __convertirJsonAListas(cls, datos):
        from modelos.bodega import Bodega
        from modelos.cepa import Cepa
        from modelos.vino import Vino
        cls.bodegas = [Bodega(**bodega) for bodega in datos['bodegas']]
        cls.cepas = [Cepa(**cepa) for cepa in datos['cepas']]
        cls.vinos = [Vino(**vino) for vino in datos['vinos']]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        return sorted(cls.bodegas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.bodegas

    @classmethod
    def buscarBodega(cls, id):
        return next((bodega for bodega in cls.bodegas if bodega.id == id), None)

    @classmethod
    def obtenerVinos(cls):
        return cls.vinos

    @classmethod
    def buscarCepa(cls, id):
        return next((cepa for cepa in cls.cepas if cepa.id == id), None)