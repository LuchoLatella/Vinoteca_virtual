# archivo: servicios/vinoteca.py
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
        cls.bodegas = [Bodega(**bodega) for bodega in datos['bodegas']]
        cls.cepas = [Cepa(**cepa) for cepa in datos['cepas']]
        cls.vinos = [Vino(**vino) for vino in datos['vinos']]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        return sorted(cls.bodegas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.bodegas

    @classmethod
    def buscarBodega(cls, id):
        return next((bodega for bodega in cls.bodegas if bodega.id == id), None)
