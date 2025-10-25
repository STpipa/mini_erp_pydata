from flask import Blueprint, request, jsonify
from app import db
from models.empresa import Empresa

empresa_bp = Blueprint("empresa_bp", __name__)

@empresa_bp.route("/", methods=["GET"])
def get_empresas():
    empresas = Empresa.query.all()
    return jsonify([e.to_dict() for e in empresas])

@empresa_bp.route("/", methods=["POST"])
def add_empresa():
    data = request.json
    nueva_empresa = Empresa(
        nombre=data.get("nombre"),
        cuit=data.get("cuit"),
        direccion=data.get("direccion")
    )
    db.session.add(nueva_empresa)
    db.session.commit()
    return jsonify(nueva_empresa.to_dict()), 201
