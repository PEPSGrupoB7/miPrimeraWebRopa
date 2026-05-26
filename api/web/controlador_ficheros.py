import os

def guardar_fichero(nombre, contenido):
    try:
        print(nombre, flush=True)
        basepath = os.path.dirname(__file__)
        ruta_fichero = os.path.join(basepath, 'static/archivos', nombre)
        print('Archivo guardado en ' + ruta_fichero, flush=True)
        contenido.save(ruta_fichero)
        respuesta = {"status": "OK"}
        code = 200
    except Exception as e:
        print("Excepcion al guardar el fichero:", e, flush=True)
        respuesta = {"status": "ERROR"}
        code = 500
    return respuesta, code

def ver_fichero(nombre):
    try:
        basepath = os.path.dirname(__file__)
        ruta_fichero = os.path.join(basepath, 'static/archivos', nombre)
        with open(ruta_fichero, 'r', encoding='utf-8', errors='replace') as f:
            salida = f.read()
        respuesta = {"status": "OK", "contenido": salida}
        code = 200
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_fichero}", flush=True)
        respuesta = {"status": "ERROR", "contenido": "Archivo no encontrado"}
        code = 404
    except Exception as e:
        print(f"Excepcion al ver el fichero: {e}", flush=True)
        respuesta = {"status": "ERROR", "contenido": ""}
        code = 500
    return respuesta, code