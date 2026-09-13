"""
Rutas para gestionar el personal (no clientes) - Solo administrador
"""

from flask import Blueprint, render_template
from flask_login import login_required
from app.models.users import User
from app.models.cliente import Cliente
from app.utils.roles import ROLES
from app.utils.decorators import requiere_admin

bp = Blueprint('empleados', __name__, url_prefix='/admin/empleados')

# Roles que cuentan como personal (excluye clientes)
ROLES_EMPLEADO = {k: ROLES[k] for k in ['administrador', 'recepcionista', 'servicio_limpieza']}

@bp.route('/')
@login_required
@requiere_admin
def index():
    personal = User.query.filter(User.rol != 'cliente').order_by(User.rol, User.usuario).all()
    clientes = {c.cedula: c for c in Cliente.query.all()}
    return render_template('empleados/index.html',
                           personal=personal,
                           roles=ROLES_EMPLEADO,
                           clientes=clientes,
                           roles_todos=ROLES)