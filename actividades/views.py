from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import *


"""
Vistas Area
"""
class AreaListarView(generic.ListView):
    """Listar las areas"""
    model = Area
    context_object_name = 'objects'
    queryset = Area.objects.all()
    template_name = 'area/listar.html'


class AreaCrearView(generic.CreateView):
    """Crear una area"""
    model = Area
    fields = ['nombre']
    template_name = 'area/crear.html'
    success_url = '/area/'


class AreaEditarView(generic.UpdateView):
    """Actualizar una area"""
    model = Area
    fields = ['nombre']
    template_name = 'area/actualizar.html'
    success_url = '/area/'


class AreaBorrarView(generic.DeleteView):
    """Eliminar una area"""
    model = Area
    template_name = 'area/eliminar.html'
    success_url = '/area/'

    def form_valid(self, form):
        messages.success(self.request, "Area eliminada de manera correcta.")
        return super(AreaBorrarView,self).form_valid(form)
    

"""
Vistas para Estado
"""
class EstadoListarView(generic.ListView):
    """Listar los estados"""
    model = Estado
    context_object_name = 'objects'
    queryset = Estado.objects.all()
    template_name = 'estado/listar.html'


class EstadoCrearView(generic.CreateView):
    """Crear un estado"""
    model = Estado
    fields = ['nombre']
    template_name = 'estado/crear.html'
    success_url = '/estado/'


class EstadoEditarView(generic.UpdateView):
    """Actualizar un estado"""
    model = Estado
    fields = ['nombre']
    template_name = 'estado/actualizar.html'
    success_url = '/estado/'


class EstadoBorrarView(generic.DeleteView):
    """Eliminar un estado"""
    model = Estado
    template_name = 'estado/eliminar.html'
    success_url = '/estado/'

    def form_valid(self, form):
        messages.success(self.request, "Estado eliminado de manera correcta.")
        return super(EstadoBorrarView, self).form_valid(form)
    

"""
Vistas para Tipo de Usuario Sello
"""    
class TipoUsuarioListarView(generic.ListView):
    """Listar los tipos de usuarios"""
    model = TipoUsuarioSello
    context_object_name = 'objects'
    queryset = TipoUsuarioSello.objects.all()
    template_name = 'tipo_usuario/listar.html'


class TipoUsuarioCrearView(generic.CreateView):
    """Crear un tipo de usuario"""
    model = TipoUsuarioSello
    fields = ['nombre']
    template_name = 'tipo_usuario/crear.html'
    success_url = '/tipo_usuario/'


class TipoUsuarioEditarView(generic.UpdateView):
    """Actualizar un tipo de usuario"""
    model = TipoUsuarioSello
    fields = ['nombre']
    template_name = 'tipo_usuario/actualizar.html'
    success_url = '/tipo_usuario/'


class TipoUsuarioBorrarView(generic.DeleteView):
    """Eliminar un tipo de usuario"""
    model = TipoUsuarioSello
    template_name = 'tipo_usuario/eliminar.html'
    success_url = '/tipo_usuario/'

    def form_valid(self, form):
        messages.success(self.request, 
                            "Tipo de usuario eliminado de manera correcta.")
        return super(TipoUsuarioBorrarView, self).form_valid(form)


"""
Vistas para Usuario Sello
"""
class UsuarioSelloListarView(generic.ListView):
    """Listar los usuarios sellos"""
    model = UsuarioSello
    context_object_name = 'objects'
    queryset = UsuarioSello.objects.all()
    template_name = 'usuario_sello/listar.html'


class UsuarioSelloCrearView(generic.CreateView):
    """Crear un usuario sello"""
    model = UsuarioSello
    fields = ['usuario_sello', 'nombre_usuario']
    template_name = 'usuario_sello/crear.html'
    success_url = '/usuario_sello/'


class UsuarioSelloEditarView(generic.UpdateView):
    """Actualizar un usuario sello"""
    model = UsuarioSello
    fields = ['usuario_sello', 'nombre_usuario']
    template_name = 'usuario_sello/actualizar.html'
    success_url = '/usuario_sello/'


class UsuarioSelloBorrarView(generic.DeleteView):
    """Eliminar un usuario sello"""
    model = UsuarioSello
    template_name = 'usuario_sello/eliminar.html'
    success_url = '/usuario_sello/'

    def form_valid(self, form):
        messages.success(self.request,
                            "Usuario sello eliminado de manera correcta.")
        return super(UsuarioSelloBorrarView, self).form_valid(form)
    

"""
Vistas para Periodo
"""
class PeriodoListarView(generic.ListView):
    """Listar los periodos"""
    model = Periodo
    context_object_name = 'objects'
    queryset = Periodo.objects.all()
    template_name = 'periodo/listar.html'


class PeriodoCrearView(generic.CreateView):
    """Crear un periodo"""
    model = Periodo
    fields = ['usuario_sello', 'year']
    template_name = 'periodo/crear.html'
    success_url = '/periodo/'


class PeriodoEditarView(generic.UpdateView):
    """Actualizar un periodo"""
    model = Periodo
    fields = ['usuario_sello', 'year']
    template_name = 'periodo/actualizar.html'
    success_url = '/periodo/'


class PeriodoBorrarView(generic.DeleteView):
    """Eliminar un periodo"""
    model = Periodo
    template_name = 'periodo/eliminar.html'
    success_url = '/periodo/'

    def form_valid(self, form):
        messages.success(self.request,
                            "Periodo eliminado de manera correcta.")
        return super(PeriodoBorrarView, self).form_valid(form)


"""
Vistas para Actividad Sello
"""
# esto se cambiara a vista basada en funcion
class ActividadSelloListarView(generic.ListView):
    """Listar las actividades sellos"""
    model = ActividadSello
    context_object_name = 'objects'
    queryset = ActividadSello.objects.all()
    template_name = 'actividad_sello/listar.html'


class ActividadSelloCrearView(generic.CreateView):
    """Crear una actividad sello"""
    model = ActividadSello
    fields = ['usuario_sello', 'periodo', 'area', 'estado', 'nombre', 
                'fecha_inicio', 'fecha_fin', 'descripcion']
    template_name = 'actividad_sello/crear.html'
    success_url = '/actividad_sello/'


class ActividadSelloEditarView(generic.UpdateView):
    """Actualizar una actividad sello"""
    model = ActividadSello
    fields = ['usuario_sello', 'periodo', 'area', 'estado', 'nombre',
                'fecha_inicio', 'fecha_fin', 'descripcion']
    template_name = 'actividad_sello/actualizar.html'
    success_url = '/actividad_sello/'


class ActividadSelloBorrarView(generic.DeleteView):
    """Eliminar una actividad sello"""
    model = ActividadSello
    template_name = 'actividad_sello/eliminar.html'
    success_url = '/actividad_sello/'

    def form_valid(self, form):
        messages.success(self.request,
                            "Actividad sello eliminado de manera correcta.")
        return super(ActividadSelloBorrarView, self).form_valid(form)