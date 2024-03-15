from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class TipoUsuarioSello(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class UsuarioSello(models.Model):
    usuario_sello = models.ForeignKey(TipoUsuarioSello, on_delete=models.PROTECT)
    nombre_usuario = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_usuario
    

class Periodo(models.Model):
    usuario_sello = models.ForeignKey(UsuarioSello, on_delete=models.PROTECT)
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    facultad = models.CharField(max_length=125)
    carrera = models.CharField(max_length=125)
    year = models.IntegerField()
    creditos = models.IntegerField()
    horas = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class ActividadSello(models.Model):
    usuario_sello = models.ForeignKey(UsuarioSello, on_delete=models.PROTECT)
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    horas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class MatriculaActividad(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    actividad_sello = models.ForeignKey(ActividadSello, on_delete=models.PROTECT)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.alumno.nombre} - {self.actividad_sello.nombre}"
