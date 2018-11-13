from django.db import models

# Create your models here.

class States(models.Model):
    id_state = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = "States"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class College(models.Model):
    id_college = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    telephone = models.IntegerField()
    address = models.CharField(max_length=200)
    class Meta:
        db_table = "College"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]


class Campus(models.Model):
    id_campus = models.IntegerField()
    state = models.ForeignKey(States,on_delete=models.PROTECT)
    college = models.ForeignKey(College,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    telephone = models.IntegerField()
    address = models.CharField(max_length=200)
    class Meta:
        db_table = "Campus"

    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class Institutes(models.Model):
    id_institute = models.IntegerField()
    campus = models.ForeignKey(Campus,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    telephone = models.IntegerField()
    address = models.CharField(max_length=200)
    class Meta:
        unique_together = (("id_institute", "campus"),)
        db_table = "Institutes"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class Subinstitutes(models.Model):
    id_subinstitute = models.AutoField(primary_key=True)
    institute = models.ForeignKey(Institutes,on_delete=models.PROTECT)
    id_reference_sub = models.ForeignKey('self',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.IntegerField()
    class Meta:
        db_table = "Subinstitutes"

    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)
    class Meta:
        db_table = "Roles"

    def __str__(self):
        """A string representation of the model."""
        return self.role[:50]

class User_profiles(models.Model):
    id_user_profile = models.AutoField(primary_key=True)
    profile = models.CharField(max_length=200)
    class Meta:
        db_table = "User_profiles"

    def __str__(self):
        """A string representation of the model."""
        return self.profile[:50]

class Papers(models.Model):
    id_paper = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    binary = models.BinaryField()
    class Meta:
        db_table = "Papers"
    def __str__(self):
        """A string representation of the model."""
        return self.topic[:50]

class People(models.Model):
    id_people = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    user_profile = models.ForeignKey(User_profiles,on_delete=models.PROTECT)
    institute = models.ForeignKey(Institutes,on_delete=models.PROTECT)
    subinstitute = models.ForeignKey(Subinstitutes,on_delete=models.PROTECT)
    role = models.ForeignKey(Roles,on_delete=models.PROTECT)
    academic_level = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    personal_telephone = models.CharField(max_length=200)
    class Meta:
        db_table = "People"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class Groups(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    id_creator = models.ForeignKey(People,on_delete=models.PROTECT)
    class Meta:
        db_table = "Groups"

    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]


class Public(models.Model):
    id_people = models.ForeignKey(People,on_delete=models.PROTECT)
    mail = models.BooleanField()
    id_institute = models.BooleanField()
    id_subinstitute = models.BooleanField()
    academic_level = models.BooleanField()
    degree = models.BooleanField()
    name = models.BooleanField()
    last_name = models.BooleanField()
    personal_telephone = models.BooleanField()
    class Meta:
        db_table = "Public"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]



