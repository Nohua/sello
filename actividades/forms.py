from crispy_forms.layout import Layout, Div, Field
from django import forms
from actividades.models import MatriculaActividad, Alumno, Estado, Periodo


class MatriculaActividadForm(forms.Form):
    alumnos = forms.ModelMultipleChoiceField(
        queryset=Alumno.objects.all(),
    )

    def __init__(self, *args, **kwargs):
        anio = kwargs.pop('anio')
        actividad_pk = kwargs.pop('actividad_pk')
        alumnos_inscritos = MatriculaActividad.objects.filter(actividad_sello__pk=actividad_pk).values_list('alumno_id', flat=True)
        super(MatriculaActividadForm, self).__init__(*args, **kwargs)
        self.fields['alumnos'].queryset = Alumno.objects.filter(year=anio).exclude(id__in=alumnos_inscritos)
        self.fields['alumnos'].widget.attrs['class'] = "form-control select2"
        self.fields['alumnos'].label = ""


class ActividadSelloFiltro(forms.Form):
    estados = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        required=False
    )
    periodos = forms.ModelChoiceField(
        queryset=Periodo.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ActividadSelloFiltro, self).__init__(*args, **kwargs)
        self.fields['estados'].widget.attrs['class'] = "select2 form-control"
        self.fields['periodos'].widget.attrs['class'] = "select2 form-control"
