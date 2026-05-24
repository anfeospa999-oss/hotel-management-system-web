from app import db
from datetime import datetime

class Comentario(db.Model):
    __tablename__ = 'comentario'
    idComentario = db.Column(db.Integer, primary_key=True)
    idHabitacion = db.Column(db.Integer, db.ForeignKey('habitacion.idHabitacion'), nullable=False)
    cedulaCliente = db.Column(db.BigInteger, db.ForeignKey('cliente.cedula'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)  # 1-5 estrellas
    comentario = db.Column(db.Text, nullable=False)
    fechaComentario = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    habitacion = db.relationship('Habitacion', backref='comentarios', lazy=True)
    cliente = db.relationship('Cliente', backref='comentarios', lazy=True)
    
    def __repr__(self):
        return f'<Comentario {self.idComentario} - Habitación {self.idHabitacion} - {self.calificacion} estrellas>'
