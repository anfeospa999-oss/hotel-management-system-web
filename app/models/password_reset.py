from app import db
from datetime import datetime, timedelta
import secrets

class PasswordResetToken(db.Model):
    __tablename__ = 'password_reset_token'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False)
    
    user = db.relationship('User', backref='reset_tokens')
    
    @staticmethod
    def generate_token(user_id):
        """Genera un token único para restablecimiento de contraseña"""
        token = secrets.token_urlsafe(32)
        expires_at = datetime.utcnow() + timedelta(hours=1)  # Token válido por 1 hora
        reset_token = PasswordResetToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at
        )
        db.session.add(reset_token)
        db.session.commit()
        return token
    
    @staticmethod
    def verify_token(token):
        """Verifica si el token es válido y no ha expirado"""
        reset_token = PasswordResetToken.query.filter_by(token=token, used=False).first()
        if reset_token and reset_token.expires_at > datetime.utcnow():
            return reset_token
        return None
    
    def mark_as_used(self):
        """Marca el token como usado"""
        self.used = True
        db.session.commit()
