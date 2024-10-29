import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request
from servicios.vinoteca import Vinoteca

app = Flask(__name__)
Vinoteca.inicializar()

@app.route("/api/bodegas")
def listar_bodegas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == 'si'
    bodegas = Vinoteca.obtenerBodegas(orden, reverso)
    return jsonify([bodega.convertirAJSON() for bodega in bodegas])

@app.route("/api/bodegas/<id>")
def obtener_bodega(id):
    bodega = Vinoteca.buscarBodega(id)
    return jsonify(bodega.convertirAJSON()) if bodega else ("Bodega no encontrada", 404)

if __name__ == "__main__":
    app.run(debug=True)
