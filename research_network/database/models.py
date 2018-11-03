from django.db import models

# Create your models here.
class Institutos(models.Model):
    id_instituto = models.AutoField(primary_key=True)
    nombre = models.TextField()
    telefono = models.IntegerField()
    class Meta:
        db_table = "Institutos"

class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.TextField()
    class Meta:
        db_table = "Estados"

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    id_instituto = models.IntegerField()
    colegio = models.IntegerField()
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.TextField()
    class Meta:
        db_table = "Departamento"

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.TextField()
    class Meta:
        db_table = "Roles"

class Grupos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    id_instituto = models.IntegerField()
    id_colegio = models.IntegerField()
    nombre = models.TextField()
    class Meta:
        db_table = "Grupos"

class Articulos(models.Model):
    id_articulo = models.AutoField(primary_key= True)
    id_instituto = models.IntegerField()
    id_colegio = models.IntegerField()
    tema = models.TextField()
    fecha_publicacion = models.TextField()
    ruta_archivo = models.TextField()
    class Meta:
        db_table = "Articulos"

class Nivel_Estudios(models.Model):
    id_nivel_estudios = models.AutoField(primary_key=True)
    nivel = models.TextField()
    class Meta:
        db_table = "Nivel_Estudios"

class Estudios(models.Model):
    id_estudios = models.AutoField(primary_key=True)
    id_instituto = models.IntegerField()
    id_colegio = models.IntegerField()
    estudio = models.TextField()
    class Meta:
        db_table = "Estudios"

class Estudios_Personas(models.Model):
    id_estudio = models.IntegerField()
    id_persona = models.IntegerField()
    class Meta:
        db_table = "Estudios_Personas"

class Colegios(models.Model):
    id_colegio = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estados,on_delete=models.PROTECT)
    instituto = models.ForeignKey(Institutos,on_delete=models.PROTECT)
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.IntegerField()
    correo = models.IntegerField()
    class Meta:
        db_table = "Colegios"

class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.TextField()
    curp = models.TextField()
    telefono = models.IntegerField()
    correo = models.TextField()
    instituto = models.ForeignKey(Institutos,on_delete=models.PROTECT)
    colegio = models.ForeignKey(Colegios,on_delete=models.PROTECT)
    estado = models.ForeignKey(Estados,on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT)
    rol = models.ForeignKey(Roles,on_delete=models.PROTECT)
    nivel_estudios = models.ForeignKey(Nivel_Estudios,on_delete=models.PROTECT)
    grupos = models.ManyToManyField(Grupos, help_text='Grupos a los que pertenece')
    articulos = models.ManyToManyField(Articulos, help_text='Articulos en los que aparece')
    estudios = models.ManyToManyField(Estudios, help_text='Estudios')
    class Meta:
        db_table = "Personas"
