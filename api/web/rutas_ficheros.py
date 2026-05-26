from flask import request, Blueprint, jsonify
from funciones_auxiliares import validar_session_normal
import controlador_ficheros

bp = Blueprint('ficheros', __name__)

EXTENSIONES_PERMITIDAS = {'txt', 'csv', 'log', 'md'}

@bp.route('/', methods=['POST'])
def upload():
    if not validar_session_normal():
        return jsonify({"status": "Forbidden"}), 403
    try:
        print(f"Form data: {request.form}", flush=True)
        print(f"Files: {request.files}", flush=True)
        contenido = request.files['fichero']
        nombre = request.form.get("nombre")
        print(f"Nombre: {nombre}", flush=True)
        if not nombre or len(nombre) > 100:
            return jsonify({"status": "Bad parameters"}), 400
        extension = contenido.filename.rsplit('.', 1)[-1].lower() if contenido.filename and '.' in contenido.filename else ''
        print(f"Archivo: {contenido.filename} | Extension: {extension}", flush=True)
        if extension not in EXTENSIONES_PERMITIDAS:
            return jsonify({"status": "ERROR", "mensaje": "Solo se permiten archivos txt, csv, log o md"}), 400
        respuesta, code = controlador_ficheros.guardar_fichero(nombre, contenido)
    except Exception as e:
        print(f"Error subiendo archivo: {e}", flush=True)
        respuesta = {"status": "ERROR"}
        code = 500
    return jsonify(respuesta), code

@bp.route('/<archivo>', methods=['GET'])
def ver(archivo):
    if not validar_session_normal():
        return jsonify({"status": "Forbidden"}), 403
    try:
        if not archivo or len(archivo) > 100:
            return jsonify({"status": "Bad parameters"}), 400
        respuesta, code = controlador_ficheros.ver_fichero(archivo)
    except Exception as e:
        print(f"Error viendo archivo: {e}", flush=True)
        respuesta = {"status": "ERROR"}
        code = 500
    return jsonify(respuesta), code