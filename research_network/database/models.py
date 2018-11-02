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
class Grupos_Personas(models.Model):
    id_persona = models.IntegerField()
    id_grupo = models.IntegerField()
    class Meta:
        db_table = "Grupos_Personas"
class Articulos(models.Model):
    id_articulo = models.AutoField(primary_key= True)
    id_instituto = models.IntegerField()
    id_colegio = models.IntegerField()
    tema = models.TextField()
    fecha_publicacion = models.TextField()
    ruta_archivo = models.TextField()
    class Meta:
        db_table = "Articulos"
class Articulos_Personas(models.Model):
    id_articulo = models.IntegerField()
    id_persona = models.IntegerField()
    class Meta:
        db_table = "Articulos_Personas"
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
    id_coloegio = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE)
    instituto = models.ForeignKey(Institutos,on_delete=models.CASCADE)
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
    instituto = models.ForeignKey(Institutos,on_delete=models.CASCADE)
    colegio = models.ForeignKey(Colegios,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles,on_delete=models.CASCADE)
    nivel_estudios = models.ForeignKey(Nivel_Estudios,on_delete=models.CASCADE)
    class Meta:
        db_table = "Personas"
