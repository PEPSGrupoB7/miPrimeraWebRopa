from flask import Flask, jsonify, request, g
from logging.config import dictConfig
from flask_wtf.csrf import CSRFProtect
from funciones_auxiliares import sanitize_field, prepare_response_extra_headers
import os

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "time-rotate": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/flask.log",
            "when": "D",
            "interval": 10,
            "backupCount": 5,
            "formatter": "default",
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console", "time-rotate"]},
})

def create_app():
    app = Flask(__name__)

    app.config.setdefault('DEBUG', True)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY')
    app.config.update(PERMANENT_SESSION_LIFETIME=600)
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
    )

    csrf = CSRFProtect(app)
    csrf.exempt('rutas_usuarios.login')
    csrf.exempt('rutas_usuarios.registro')

    extra_headers = prepare_response_extra_headers(True)

    from rutas_usuarios import bp as usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
    from rutas_chuches import bp as chuches_bp
    app.register_blueprint(chuches_bp, url_prefix='/api/chuches')
    from rutas_ficheros import bp as ficheros_bp
    app.register_blueprint(ficheros_bp, url_prefix='/api/ficheros')
    from rutas_comentarios import bp as comentarios_bp
    app.register_blueprint(comentarios_bp, url_prefix='/api/comentarios')

    @app.before_request
    def clean_request():
        if request.is_json:
            data = request.get_json(silent=True)
            if data is not None:
                g.cleaned_json = sanitize_field(data)
            else:
                g.cleaned_json = {}
        else:
            g.cleaned_json = {}

    @app.after_request
    def after_request(response):
        response.headers['Server'] = 'API'
        app.logger.info(
            "path: %s | method: %s | status: %s | size: %s >>> %s",
            request.path,
            request.method,
            response.status,
            response.content_length,
            request.remote_addr,
        )
        response.headers.extend(extra_headers)
        return response

    @app.errorhandler(500)
    def server_error(error):
        ret = {"status": "Internal Server Error"}
        return jsonify(ret), 500

    return app

if __name__ == '__main__':
    app = create_app()
    try:
        port = int(os.environ.get('PORT'))
        host = os.environ.get('HOST')
        app.run(host=host, port=port)
    except:
        print("Error starting server", flush=True)