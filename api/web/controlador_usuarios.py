from bd import obtener_conexion
from flask_wtf.csrf import generate_csrf
from funciones_auxiliares import cipher_password, compare_password, create_session

def login_usuario(username, password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT perfil, clave FROM usuarios WHERE usuario = %s",
                (username,)
            )
            usuario = cursor.fetchone()

        if usuario is None:
            ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
        else:
            perfil = usuario[0]
            password_hash = usuario[1]
            print(f"Hash de BD: {password_hash}", flush=True)
            print(f"Password recibido: {password}", flush=True)
            resultado = compare_password(password_hash, password)
            print(f"Resultado compare: {resultado}", flush=True)
            if resultado:
                create_session(username, perfil)
                ret = {
                    "status": "OK",
                    "csrf_token": generate_csrf(),
                    "perfil": perfil
                }
            else:
                ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
        code = 200
        conexion.close()
    except Exception as e:
        print("Excepcion al validar al usuario:", e, flush=True)
        ret = {"status": "ERROR"}
        code = 500
    return ret, code

def alta_usuario(username, password, perfil):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT perfil FROM usuarios WHERE usuario = %s", (username,)
            )
            usuario = cursor.fetchone()
            if usuario is None:
                password_cifrada = cipher_password(password)
                cursor.execute(
                    "INSERT INTO usuarios(usuario, clave, perfil) VALUES (%s, %s, %s)",
                    (username, password_cifrada, perfil)
                )
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret = {"status": "OK"}
                    code = 200
                else:
                    ret = {"status": "ERROR"}
                    code = 500
            else:
                ret = {"status": "ERROR", "mensaje": "Usuario ya existe"}
                code = 200
        conexion.close()
    except Exception as e:
        print("Excepcion al registrar al usuario:", e, flush=True)
        ret = {"status": "ERROR"}
        code = 500
    return ret, code

def logout():
    return {"status": "OK"}, 200