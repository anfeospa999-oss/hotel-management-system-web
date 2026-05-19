"""
Script de migración para renombrar el campo 'atendido_por' a 'recepcionista_id' en la tabla de reservas.
Este script es útil para entornos de producción (como PostgreSQL en Docker).
"""

import os
import sys

# Agregar el directorio raíz al path para que las importaciones de 'app' funcionen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

def migrate():
    app = create_app()
    
    with app.app_context():
        inspector = db.inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('reserva')]
        
        if 'recepcionista_id' in columns:
            print("El campo 'recepcionista_id' ya existe. No se requiere migración.")
            return
            
        if 'atendido_por' in columns:
            try:
                with db.engine.connect() as conn:
                    # En PostgreSQL y SQLite >= 3.25 se puede renombrar la columna directamente
                    conn.execute(db.text("ALTER TABLE reserva RENAME COLUMN atendido_por TO recepcionista_id"))
                    conn.commit()
                print("Migración exitosa: Columna 'atendido_por' renombrada a 'recepcionista_id'.")
            except Exception as e:
                print(f"Error durante la migración: {e}")
        else:
            print("No se encontró ni 'atendido_por' ni 'recepcionista_id'. Es posible que la tabla no esté inicializada correctamente.")

if __name__ == '__main__':
    migrate()
