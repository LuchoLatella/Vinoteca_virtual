import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request
from servicios.vinoteca import Vinoteca

app = Flask(__name__)
Vinoteca.inicializar()

# Ruta para obtener información de una bodega por ID
@app.route("/api/bodegas/<id>")
def obtener_bodega(id):
    bodega = Vinoteca.buscarBodega(id)
    return jsonify(bodega.convertirAJSONFull()) if bodega else ("Bodega no encontrada", 404)

# Ruta para obtener el listado de bodegas
@app.route("/api/bodegas")
def listar_bodegas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == 'si'
    bodegas = Vinoteca.obtenerBodegas(orden, reverso)
    return jsonify([bodega.convertirAJSON() for bodega in bodegas])

# Ruta para obtener información de una cepa por ID
@app.route("/api/cepas/<id>")
def obtener_cepa(id):
    cepa = Vinoteca.buscarCepa(id)
    return jsonify(cepa.convertirAJSONFull()) if cepa else ("Cepa no encontrada", 404)

# Ruta para obtener el listado de cepas
@app.route("/api/cepas")
def listar_cepas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == 'si'
    cepas = Vinoteca.obtenerCepas(orden, reverso)
    return jsonify([cepa.convertirAJSON() for cepa in cepas])

# Ruta para obtener información de un vino por ID
@app.route("/api/vinos/<id>")
def obtener_vino(id):
    vino = Vinoteca.buscarVino(id)
    return jsonify(vino.convertirAJSONFull()) if vino else ("Vino no encontrado", 404)

# Ruta para obtener el listado de vinos
@app.route("/api/vinos")
def listar_vinos():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == 'si'
    anio = request.args.get('anio', type=int)
    vinos = Vinoteca.obtenerVinos(anio, orden, reverso)
    return jsonify([vino.convertirAJSON() for vino in vinos])

if __name__ == "__main__":
    app.run(debug=True)
