from bd import obtener_conexion
from funciones_auxiliares import sanitize_field

def convertir_comentario_a_json(comentario):
    d = {}
    d['id'] = comentario[0]
    d['usuario'] = sanitize_field(comentario[1])
    d['descripcion'] = sanitize_field(comentario[2])
    return d

def insertar_comentario(usuario, descripcion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO comentarios(usuario, descripcion) VALUES (%s, %s)",
                (usuario, descripcion)
            )
            conexion.commit()
        conexion.close()
        ret = {"status": "OK"}
        code = 200
    except Exception as e:
        print("Excepcion al insertar un comentario:", e, flush=True)
        ret = {"status": "ERROR"}
        code = 500
    return ret, code

def obtener_comentarios():
    comentariosjson = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, usuario, descripcion FROM comentarios")
            comentarios = cursor.fetchall()
            if comentarios:
                for comentario in comentarios:
                    comentariosjson.append(convertir_comentario_a_json(comentario))
        conexion.close()
        code = 200
    except Exception as e:
        print("Excepcion al consultar comentarios:", e, flush=True)
        code = 500
    return comentariosjson, code