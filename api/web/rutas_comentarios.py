from flask import request, Blueprint, jsonify, g
from funciones_auxiliares import validar_session_normal
import controlador_comentarios

bp = Blueprint('comentarios', __name__)

@bp.route("/", methods=['POST'])
def guardar_comentario():
    if not validar_session_normal():
        return jsonify({"status": "Forbidden"}), 403
    if request.headers.get('Content-Type') == 'application/json':
        comentario_json = g.cleaned_json
        usuario = comentario_json.get('usuario', '')
        descripcion = comentario_json.get('descripcion', '')
        if isinstance(usuario, str) and isinstance(descripcion, str) and len(usuario) < 50 and len(descripcion) < 255:
            respuesta, code = controlador_comentarios.insertar_comentario(usuario, descripcion)
        else:
            respuesta = {"status": "Bad parameters"}
            code = 400
    else:
        respuesta = {"status": "Bad request"}
        code = 401
    return jsonify(respuesta), code

@bp.route("/", methods=['GET'])
def consultaComentarios():
    respuesta, code = controlador_comentarios.obtener_comentarios()
    return jsonify(respuesta), code