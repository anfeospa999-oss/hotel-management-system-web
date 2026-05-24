from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models.notificacion import Notificacion

bp = Blueprint('notificaciones', __name__, url_prefix='/notificaciones')

@bp.route('/')
@login_required
def index():
    """Ver todas las notificaciones del usuario"""
    notificaciones = Notificacion.query.filter_by(usuario_id=current_user.id).order_by(Notificacion.fecha_creacion.desc()).all()
    
    # Contar notificaciones no leídas
    no_leidas = Notificacion.query.filter_by(usuario_id=current_user.id, leida=False).count()
    
    return render_template('notificaciones/index.html', notificaciones=notificaciones, no_leidas=no_leidas)

@bp.route('/marcar-leida/<int:id>', methods=['POST'])
@login_required
def marcar_leida(id):
    """Marcar una notificación como leída"""
    notificacion = Notificacion.query.get_or_404(id)
    
    if notificacion.usuario_id != current_user.id:
        flash('No tienes permiso para modificar esta notificación', 'error')
        return redirect(url_for('notificaciones.index'))
    
    notificacion.marcar_como_leida()
    
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify({'success': True})
    
    return redirect(url_for('notificaciones.index'))

@bp.route('/marcar-todas-leidas', methods=['POST'])
@login_required
def marcar_todas_leidas():
    """Marcar todas las notificaciones como leídas"""
    Notificacion.query.filter_by(usuario_id=current_user.id, leida=False).update({'leida': True})
    db.session.commit()
    
    flash('Todas las notificaciones han sido marcadas como leídas', 'success')
    return redirect(url_for('notificaciones.index'))

@bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar(id):
    """Eliminar una notificación"""
    notificacion = Notificacion.query.get_or_404(id)
    
    if notificacion.usuario_id != current_user.id:
        flash('No tienes permiso para eliminar esta notificación', 'error')
        return redirect(url_for('notificaciones.index'))
    
    db.session.delete(notificacion)
    db.session.commit()
    
    flash('Notificación eliminada', 'success')
    return redirect(url_for('notificaciones.index'))

@bp.route('/contador-no-leidas')
@login_required
def contador_no_leidas():
    """Obtener el contador de notificaciones no leídas (para AJAX)"""
    no_leidas = Notificacion.query.filter_by(usuario_id=current_user.id, leida=False).count()
    return jsonify({'no_leidas': no_leidas})
