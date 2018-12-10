from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here

class States(models.Model):
    id_state = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = "States"
    def __str__(self):
        """A string representation of the model."""
        return self.name

class College(models.Model):
    id_college = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "College"
    def __str__(self):
        """A string representation of the model."""
        return self.name

class Campus(models.Model):
    id_campus = models.AutoField(primary_key=True)
    state = models.ForeignKey(States,on_delete=models.PROTECT)
    college = models.ForeignKey(College,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "Campus"

    def __str__(self):
        """A string representation of the model."""
        return self.name

class Institutes(models.Model):
    id_institute = models.AutoField(primary_key=True)
    campus = models.ForeignKey(Campus,on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    url_name_institute = models.CharField(max_length=200)
    class Meta:
        unique_together = (("id_institute", "campus"),)
        db_table = "Institutes"
    def __str__(self):
        """A string representation of the model."""
        return self.name

class Subinstitutes(models.Model):
    id_subinstitute = models.AutoField(primary_key=True)
    institute = models.ForeignKey(Institutes,on_delete=models.PROTECT)
    id_reference_sub = models.ForeignKey('self',on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "Subinstitutes"

    def __str__(self):
        """A string representation of the model."""
        return self.name

class Papers(models.Model):
    id_paper = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    file = models.FileField(upload_to='articles/')
    class Meta:
        db_table = "Papers"
    def __str__(self):
        """A string representation of the model."""
        return self.topic

class Groups(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = "Groups"

    def __str__(self):
        """A string representation of the model."""
        return self.name

class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url_name = models.CharField(max_length=200)
    id_people = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    academic_level = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    personal_telephone = models.CharField(max_length=200, null=True, blank=True)
    state = models.ForeignKey(States, on_delete=models.PROTECT)
    subinstitute = models.ForeignKey(Subinstitutes,on_delete=models.PROTECT)
    institute = models.ForeignKey(Institutes,on_delete=models.PROTECT)
    groups = models.    ManyToManyField(Groups)
    papers = models.ManyToManyField(Papers)
    class Meta:
        db_table = "People"
    def __str__(self):
        """A string representation of the model."""
        return self.name

class Public(models.Model):
    id_people = models.ForeignKey(People,on_delete=models.PROTECT)
    email = models.BooleanField()
    id_institute = models.BooleanField()
    id_subinstitute = models.BooleanField(null=True, blank=True)
    academic_level = models.BooleanField(null=True, blank=True)
    degree = models.BooleanField(null=True, blank=True)
    name = models.BooleanField()
    personal_telephone = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = "Public"
    def __str__(self):
        """A string representation of the model."""
        return self.name




