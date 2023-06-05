from django.db import models

# Create your models here.
from BasicEntry.models import District,Qualification



gender=(
    ("Male","Male"),
    ("Female","Female")
)

class Doctor(models.Model):
    District=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    DoctorName=models.CharField(max_length=20,null=False)
    DoctorGender=models.CharField(max_length=20,null=False,choices=gender)
    DoctorContact=models.CharField(max_length=20,null=False)
    DoctorEmail=models.EmailField(max_length=20,null=False,unique=True)
    HospitalAddress=models.TextField(null=False)
    QualCertificate=models.FileField(upload_to="Uploads/DoctorCertificate/",null=False)
    DoctorPhoto=models.FileField(upload_to="Uploads/DoctorImage/",null=False)
    DoctorUsername=models.CharField(max_length=20,null=False)
    DoctorPassword=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.DoctorName

class DrQualification(models.Model):
    Doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    Qualification=models.ForeignKey(Qualification,on_delete=models.SET_NULL,null=True)

class AdminRegister(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)