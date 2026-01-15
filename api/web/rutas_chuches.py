from flask import request, Blueprint, jsonify
import controlador_chuches

bp = Blueprint('chuches', __name__)

@bp.route("/", methods=["GET"])
def chuches():
    respuesta, code = controlador_chuches.obtener_chuches()
    return jsonify(respuesta), code

@bp.route("/<int:id>", methods=["GET"])
def chuche_por_id(id):
    respuesta, code = controlador_chuches.obtener_chuche_por_id(id)
    return jsonify(respuesta), code

@bp.route("/", methods=["POST"])
def guardar_chuche():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.json
        respuesta, code = controlador_chuches.insertar_chuche(
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["talla"],
            data["color"],
            data["categoria"],
            data["foto"]
        )
    else:
        respuesta = {"status": "Bad request"}
        code = 400
    return jsonify(respuesta), code

@bp.route("/<int:id>", methods=["DELETE"])
def eliminar_chuche(id):
    respuesta, code = controlador_chuches.eliminar_chuche(id)
    return jsonify(respuesta), code

@bp.route("/", methods=["PUT"])
def actualizar_chuche():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.json
        respuesta, code = controlador_chuches.actualizar_chuche(
            data["id"],
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["talla"],
            data["color"],
            data["categoria"],
            data["foto"]
        )
    else:
        respuesta = {"status": "Bad request"}
        code = 400
    return jsonify(respuesta), code
