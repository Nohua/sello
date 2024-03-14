from django.urls import path
from .views import *

urlpatterns = [ 
    # rutas para las vistas de areas
    path('area/', AreaListarView.as_view(), name='area'),
    path('area/crear', AreaCrearView.as_view(), name='area-crear'),
    path('area/editar/<int:pk>', AreaEditarView.as_view(), name='area-editar'),
    path('area/borrar/<int:pk>', 
            AreaBorrarView.as_view(), 
            name='area-borrar'),
    # rutas para las vistas de estados
    path('estado/', EstadoListarView.as_view(), name='estado'),
    path('estado/crear', EstadoCrearView.as_view(), name='estado-crear'),
    path('estado/editar/<int:pk>', 
            EstadoEditarView.as_view(),
            name='estado-editar'),
    path('estado/borrar/<int:pk>', 
            EstadoBorrarView.as_view(),
            name='estado-borrar'),
    # rutas para las vistas de tipos de usuarios
    path('tipo_usuario/', 
            TipoUsuarioListarView.as_view(),
            name='tipo-usuario'), 
    path('tipo_usuario/crear',
            TipoUsuarioCrearView.as_view(),
            name='tipo-usuario-crear'),
    path('tipo_usuario/editar/<int:pk>',
            TipoUsuarioEditarView.as_view(),
            name='tipo-usuario-editar'),
    path('tipo_usuario/borrar/<int:pk>',
            TipoUsuarioBorrarView.as_view(),
            name='tipo-usuario-borrar'),
    # rutas para las vistas de usuarios sellos
    path('usuario_sello/',
            UsuarioSelloListarView.as_view(),
            name='usuario-sello'),
    path('usuario_sello/crear',
            UsuarioSelloCrearView.as_view(),
            name='usuario-sello-crear'),
    path('usuario_sello/editar/<int:pk>',
            UsuarioSelloEditarView.as_view(),
            name='usuario-sello-editar'),
    path('usuario_sello/borrar/<int:pk>',
            UsuarioSelloBorrarView.as_view(),
            name='usuario-sello-borrar'),
    # rutas para las vistas de periodos
    path('periodo/', PeriodoListarView.as_view(), name='periodo'),
    path('periodo/crear', PeriodoCrearView.as_view(), name='periodo-crear'),
    path('periodo/editar/<int:pk>',
            PeriodoEditarView.as_view(),
            name='periodo-editar'),
    path('periodo/borrar/<int:pk>',
            PeriodoBorrarView.as_view(),
            name='periodo-borrar'),
    # rutas para las vistas de actividades sello
    path('actividad_sello/',
            ActividadSelloListarView.as_view(),
            name='actividad-sello'),
    path('actividad_sello/crear',
            ActividadSelloCrearView.as_view(),
            name='actividad-sello-crear'),
    path('actividad_sello/editar/<int:pk>',
            ActividadSelloEditarView.as_view(),
            name='actividad-sello-editar'),
    path('actividad_sello/borrar/<int:pk>',
            ActividadSelloBorrarView.as_view(),
            name='actividad-sello-borrar'),
]
