from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

"""
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        New_User.objects.create(user=instance)
    instance.profile.save()
"""

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    class Meta:
        db_table = "UserProfileInfo"
    def __str__(self):
        return self.user.username

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
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "College"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

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
        return self.name[:50]

class Institutes(models.Model):
    id_institute = models.AutoField(primary_key=True)
    campus = models.ForeignKey(Campus,on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        unique_together = (("id_institute", "campus"),)
        db_table = "Institutes"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

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
    file_path = models.CharField(max_length=200, null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)
    class Meta:
        db_table = "Papers"
    def __str__(self):
        """A string representation of the model."""
        return self.topic[:50]

class Groups(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = "Groups"

    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class People(models.Model):
    id_people = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    user_profile = models.ForeignKey(User_profiles,on_delete=models.PROTECT)
    institute = models.ForeignKey(Institutes,on_delete=models.PROTECT)
    subinstitute = models.ForeignKey(Subinstitutes,on_delete=models.PROTECT, null=True, blank=True)
    role = models.ForeignKey(Roles,on_delete=models.PROTECT)
    academic_level = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    groups = models.ManyToManyField(Groups, null=True, blank=True)
    personal_telephone = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "People"
    def __str__(self):
        """A string representation of the model."""
        return self.name[:50]

class Public(models.Model):
    id_people = models.ForeignKey(People,on_delete=models.PROTECT)
    mail = models.BooleanField()
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
        return self.name[:50]

class New_User(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_new_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    academic_level = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    personal_telephone = models.CharField(max_length=200, null=True, blank=True)
    id_institute = models.ForeignKey(Institutes, on_delete=models.PROTECT)
    id_subinstitute = models.ForeignKey(Subinstitutes, on_delete=models.PROTECT)
    id_user_profile = models.ForeignKey(User_profiles, on_delete=models.PROTECT)
    class Meta:
        db_table = "New_User"

class Modify_User(models.Model):
    id_modify_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    academic_level = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    personal_telephone = models.CharField(max_length=200, null=True, blank=True)
    id_people = models.ForeignKey(People, on_delete=models.PROTECT)
    id_institute = models.ForeignKey(Institutes, on_delete= models.PROTECT)
    id_subinstitute = models.ForeignKey(Subinstitutes, on_delete= models.PROTECT)
    class Meta:
        db_table = "Modify_User"

class Remove_Document(models.Model):
    id_remove_document = models.AutoField(primary_key=True)
    id_paper = models.ForeignKey(Papers, on_delete= models.PROTECT)
    class Meta:
        db_table = "Remove_Document"

class Upload_Document(models.Model):
    id_upload_document = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200, null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)
    class  Meta:
        db_table = "Upload_Document"

class Join_Group(models.Model):
    id_join_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    id_people = models.ForeignKey(People, on_delete= models.PROTECT)
    class Meta:
        db_table = "Join_Group"

class Register_Place(models.Model):
    id_register_place = models.AutoField(primary_key=True)
    type_place = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    telephone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    id_state = models.ForeignKey(States, on_delete= models.PROTECT)
    class Meta:
        db_table = "Register_Place"

class Modify_Place(models.Model):
    id_modify_place = models.AutoField(primary_key=True)
    id_institute = models.ForeignKey(Institutes, on_delete=models.PROTECT)
    id_subinstitute = models.ForeignKey(Subinstitutes, on_delete= models.PROTECT)
    id_campus = models.ForeignKey(Campus, on_delete= models.PROTECT)
    id_state = models.ForeignKey(States, on_delete= models.PROTECT)
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = "Modify_Place"

class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_new_user = models.ForeignKey(New_User, on_delete=models.PROTECT)
    id_modify_user = models.ForeignKey(Modify_User, on_delete=models.PROTECT)
    id_upload_document = models.ForeignKey(Upload_Document, on_delete=models.PROTECT)
    id_remove_document = models.ForeignKey(Remove_Document, on_delete=models.PROTECT)
    id_join_group = models.ForeignKey(Join_Group, on_delete=models.PROTECT)
    id_register_place = models.ForeignKey(Register_Place, on_delete=models.PROTECT)
    id_modify_place = models.ForeignKey(Modify_Place, on_delete=models.PROTECT)
    class Meta:
        db_table = "Events"

class Log(models.Model):
    autor_event = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    description = models.TextField()
    id_event = models.ForeignKey(Events, on_delete=models.PROTECT)
    class Meta:
        db_table = "Log"

class Requests(models.Model):
    id_request = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events, on_delete=models.PROTECT)
    id_people_receiver = models.ForeignKey(People, on_delete=models.PROTECT)
    class Meta:
        db_table = "Requests"
