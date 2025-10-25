from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from routes.empresas_routes import empresas_bp
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar base de datos
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar con app
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar los Blueprints
    app.register_blueprint(empresas_bp, url_prefix="/api/empresas")

    @app.route("/")
    def home():
        return {"mensaje": "Bienvenido al mini ERP PyData"}

    return app

# Ejecutar servidor Flask
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
