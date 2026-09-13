# -*- coding: utf-8 -*-
# Este archivo fuerza a Babel a extraer los strings de valores de BD
# para que aparezcan en el catálogo de traducciones.
# NO ejecutar este archivo directamente.

from flask_babel import gettext as _

# Roles
_('Administrador')
_('Recepcionista')
_('Servicio Limpieza')
_('Cliente')
_('Contador')
_('Camarero')

# Estados de reserva
_('Pendiente')
_('Confirmada')
_('Finalizada')
_('Cancelada')
_('Ocupada')
_('En Limpieza')

# Estados de habitación
_('Disponible')
_('Mantenimiento')
_('Limpieza')

# Estados de limpieza
_('En Curso')
_('Finalizado')
_('Pendiente de Limpieza')
_('Completada')

# Otros valores de BD que se muestran en UI
_('No especificada')
_('Sin historial de reservas')
