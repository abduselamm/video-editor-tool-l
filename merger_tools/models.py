from django.db import models

from django.core.validators import FileExtensionValidator
from time import timezone
# Create your models here.

class O_Video(models.Model):
    original_video = models.FileField(upload_to='original_uploaded',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class M_Video(models.Model):
    merged_video = models.FileField(upload_to='merged_uploaded',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)

""" class Scale(models.Model):
    s = (
        ('one_with_one', "One with one"),
        ('one_with_many', "One with many")
    )
    scale_type = models.CharField(max_length=20, choices=s, null=True) 

class Cut_Original(models.Model):
    cut_original = models.FileField(upload_to='cut_original',null=True)
    #v = models.CharField(max_length=10000, null=True)"""

class Zip_file(models.Model):
    file = models.FileField(upload_to='zip',null=True)
    def __str__(self):
        return self.file
class Output_Video(models.Model):
    output = models.FileField(upload_to='output_video', null=True)      

class MetaData_Video(models.Model):
    video = models.FileField(upload_to='metadata', null=True)      

class Folder(models.Model):
    folder = models.CharField(max_length=200,null=True)
    def __str__(self) -> str:
        return self.folder
    
class New_Metadata(models.Model):
    fold = models.ForeignKey(Folder, null=True, on_delete=models.CASCADE)
    new_video=models.FileField(upload_to='newVideo', null=True)
    def __str__(self) -> str:
        return self.fold.folder
    
