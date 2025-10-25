from app import db

class Empresa(db.Model):
    __tablename__ = "empresas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cuit = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(200))

    def __repr__(self):
        return f"<Empresa {self.nombre}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cuit": self.cuit,
            "direccion": self.direccion
        }
