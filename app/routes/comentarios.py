from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.comentario import Comentario
from app.models.habitacion import Habitacion
from app.models.reserva import Reserva
from app.utils.decorators import requiere_permiso

bp = Blueprint('comentarios', __name__, url_prefix='/comentarios')

@bp.route('/habitacion/<int:id_habitacion>')
@login_required
def ver_comentarios_habitacion(id_habitacion):
    """Ver todos los comentarios de una habitación específica"""
    habitacion = Habitacion.query.get_or_404(id_habitacion)
    comentarios = Comentario.query.filter_by(idHabitacion=id_habitacion).order_by(Comentario.fechaComentario.desc()).all()
    
    # Calcular promedio de calificaciones
    if comentarios:
        promedio = sum(c.calificacion for c in comentarios) / len(comentarios)
    else:
        promedio = 0
    
    return render_template('comentarios/habitacion.html', 
                          habitacion=habitacion, 
                          comentarios=comentarios, 
                          promedio=promedio)

@bp.route('/nuevo/<int:id_habitacion>', methods=['GET', 'POST'])
@login_required
def nuevo_comentario(id_habitacion):
    """Crear un nuevo comentario para una habitación"""
    # Verificar que el usuario sea un cliente
    if current_user.rol != 'cliente':
        flash('Solo los clientes pueden dejar comentarios', 'error')
        return redirect(url_for('habitaciones.index'))
    
    habitacion = Habitacion.query.get_or_404(id_habitacion)
    
    # Verificar que el cliente haya tenido una reserva en esta habitación
    reserva_previa = Reserva.query.filter(
        Reserva.cedulaCliente == current_user.cedula,
        Reserva.idHabitacion == id_habitacion,
        Reserva.estadoReserva == 'finalizada'
    ).first()
    
    if not reserva_previa:
        flash('Solo puedes comentar sobre habitaciones donde te has hospedado', 'warning')
        return redirect(url_for('habitaciones.detalle', id=id_habitacion))
    
    # Verificar si ya comentó esta habitación
    comentario_existente = Comentario.query.filter_by(
        idHabitacion=id_habitacion,
        cedulaCliente=current_user.cedula
    ).first()
    
    if comentario_existente:
        flash('Ya has dejado un comentario para esta habitación', 'warning')
        return redirect(url_for('comentarios.ver_comentarios_habitacion', id_habitacion=id_habitacion))
    
    if request.method == 'POST':
        calificacion = request.form.get('calificacion')
        comentario_texto = request.form.get('comentario')
        
        # Validaciones
        if not calificacion or not comentario_texto:
            flash('Por favor completa todos los campos', 'error')
            return redirect(url_for('comentarios.nuevo_comentario', id_habitacion=id_habitacion))
        
        try:
            calificacion = int(calificacion)
            if calificacion < 1 or calificacion > 5:
                flash('La calificación debe estar entre 1 y 5 estrellas', 'error')
                return redirect(url_for('comentarios.nuevo_comentario', id_habitacion=id_habitacion))
        except ValueError:
            flash('Calificación inválida', 'error')
            return redirect(url_for('comentarios.nuevo_comentario', id_habitacion=id_habitacion))
        
        if len(comentario_texto) < 10:
            flash('El comentario debe tener al menos 10 caracteres', 'error')
            return redirect(url_for('comentarios.nuevo_comentario', id_habitacion=id_habitacion))
        
        if len(comentario_texto) > 500:
            flash('El comentario no puede exceder 500 caracteres', 'error')
            return redirect(url_for('comentarios.nuevo_comentario', id_habitacion=id_habitacion))
        
        nuevo_comentario = Comentario(
            idHabitacion=id_habitacion,
            cedulaCliente=current_user.cedula,
            calificacion=calificacion,
            comentario=comentario_texto
        )
        
        db.session.add(nuevo_comentario)
        db.session.commit()
        
        flash('¡Gracias por tu comentario!', 'success')
        return redirect(url_for('comentarios.ver_comentarios_habitacion', id_habitacion=id_habitacion))
    
    return render_template('comentarios/nuevo.html', habitacion=habitacion)

@bp.route('/mis-comentarios')
@login_required
def mis_comentarios():
    """Ver todos los comentarios del usuario actual"""
    if current_user.rol != 'cliente':
        flash('Esta función es solo para clientes', 'error')
        return redirect(url_for('auth.menu'))
    
    comentarios = Comentario.query.filter_by(cedulaCliente=current_user.cedula).order_by(Comentario.fechaComentario.desc()).all()
    return render_template('comentarios/mis_comentarios.html', comentarios=comentarios)

@bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_comentario(id):
    """Eliminar un comentario propio"""
    comentario = Comentario.query.get_or_404(id)
    
    # Verificar que el comentario sea del usuario actual
    if comentario.cedulaCliente != current_user.cedula:
        flash('No tienes permiso para eliminar este comentario', 'error')
        return redirect(url_for('comentarios.mis_comentarios'))
    
    db.session.delete(comentario)
    db.session.commit()
    
    flash('Comentario eliminado correctamente', 'success')
    return redirect(url_for('comentarios.mis_comentarios'))
