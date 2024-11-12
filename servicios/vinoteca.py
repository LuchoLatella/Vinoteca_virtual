import json
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

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
        cls.bodegas = [Bodega(**b) for b in datos['bodegas']]
        cls.cepas = [Cepa(**c) for c in datos['cepas']]
        cls.vinos = [Vino(**v) for v in datos['vinos']]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        return sorted(cls.bodegas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        return sorted(cls.cepas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.vinos
        if anio:
            vinos = [vino for vino in vinos if anio in vino.partidas]
        return sorted(vinos, key=lambda x: getattr(x, orden), reverse=reverso) if orden else vinos

    @classmethod
    def buscarBodega(cls, id):
        return next((b for b in cls.bodegas if b.id == id), None)

    @classmethod
    def buscarCepa(cls, id):
        return next((c for c in cls.cepas if c.id == id), None)

    @classmethod
    def buscarVino(cls, id):
        return next((v for v in cls.vinos if v.id == id), None)
