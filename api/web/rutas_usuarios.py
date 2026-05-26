from flask import request, Blueprint, jsonify, g
from funciones_auxiliares import Encoder, delete_session, validar_session_normal
import controlador_usuarios

bp = Blueprint('usuarios', __name__)

@bp.route("/login", methods=['POST'])
def login():
    if request.headers.get('Content-Type') == 'application/json':
        login_json = g.cleaned_json
        username = login_json.get("username", "")
        password = login_json.get("password", "")
        if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
            respuesta, code = controlador_usuarios.login_usuario(username, password)
        else:
            respuesta = {"status": "Bad parameters"}
            code = 401
    else:
        respuesta = {"status": "Bad request"}
        code = 401
    return jsonify(respuesta), code

@bp.route("/registro", methods=['POST'])
def registro():
    if request.headers.get('Content-Type') == 'application/json':
        login_json = g.cleaned_json
        username = login_json.get("username", "")
        password = login_json.get("password", "")
        profile = login_json.get("profile", "normal")
        if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
            respuesta, code = controlador_usuarios.alta_usuario(username, password, profile)
        else:
            respuesta = {"status": "Bad parameters"}
            code = 401
    else:
        respuesta = {"status": "Bad request"}
        code = 401
    return jsonify(respuesta), code

@bp.route("/logout", methods=['GET'])
def logout():
    try:
        delete_session()
        ret = {"status": "OK"}
        code = 200
    except:
        ret = {"status": "ERROR"}
        code = 500
    return jsonify(ret), code