from bd import obtener_conexion
from funciones_auxiliares import sanitize_field


def convertir_chuche_a_json(ropa):
    d = {}
    d['id'] = ropa[0]
    d['nombre'] = sanitize_field(ropa[1])
    d['descripcion'] = sanitize_field(ropa[2])
    d['precio'] = float(ropa[3])
    d['talla'] = sanitize_field(ropa[4])
    d['color'] = sanitize_field(ropa[5])
    d['categoria'] = sanitize_field(ropa[6])
    d['foto'] = sanitize_field(ropa[7])
    return d


def insertar_chuche(nombre, descripcion, precio, talla, color, categoria, foto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO ropa (nombre, descripcion, precio, talla, color, categoria, foto)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (nombre, descripcion, precio, talla, color, categoria, foto)
        )
    conexion.commit()
    conexion.close()
    ret = {"status": "OK"}
    code = 200
    return ret, code


def obtener_chuches():
    ropajson = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, nombre, descripcion, precio, talla, color, categoria, foto
                FROM ropa
                """
            )
            ropa = cursor.fetchall()
            for prenda in ropa:
                ropajson.append(convertir_chuche_a_json(prenda))
        conexion.close()
        code = 200
    except Exception as e:
        print("Excepcion al consultar toda la ropa:", e, flush=True)
        code = 500
    return ropajson, code


def obtener_chuche_por_id(id):
    prenda_json = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, nombre, descripcion, precio, talla, color, categoria, foto
                FROM ropa WHERE id = %s
                """,
                (id,)
            )
            prenda = cursor.fetchone()
            if prenda is not None:
                prenda_json = convertir_chuche_a_json(prenda)
        conexion.close()
        code = 200
    except Exception as e:
        print("Excepcion al consultar una prenda:", e, flush=True)
        code = 500
    return prenda_json, code


def eliminar_chuche(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM ropa WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except Exception as e:
        print("Excepcion al eliminar una prenda:", e, flush=True)
        ret = {"status": "Failure"}
        code = 500
    return ret, code


def actualizar_chuche(id, nombre, descripcion, precio, talla, color, categoria, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE ropa
                SET nombre = %s,
                    descripcion = %s,
                    precio = %s,
                    talla = %s,
                    color = %s,
                    categoria = %s,
                    foto = %s
                WHERE id = %s
                """,
                (nombre, descripcion, precio, talla, color, categoria, foto, id)
            )
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except Exception as e:
        print("Excepcion al actualizar una prenda:", e, flush=True)
        ret = {"status": "Failure"}
        code = 500
    return ret, code
