from django.db import models

# Create your models here.
from Admin.models import Doctor

class Videos(models.Model):
    VideosCaption=models.CharField(max_length=20,null=False)
    VideosDescription=models.TextField(max_length=20,null=False)
    VideosVideo=models.FileField(upload_to="Uploads/MedicalVideos/",null=False)
    VideoDate=models.DateField(auto_now_add=True)
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    
    