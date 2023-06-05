from django.db import models

# Create your models here.
from BasicEntry.models import *
from Guest.models import Customer
from Admin.models import Doctor
from ShopOwner.models import PetSale,Product


class Pet(models.Model): 
    Petcolor=models.CharField(max_length=20,null=False)
    PetGender=models.CharField(max_length=20,null=False)
    PetBreed=models.CharField(max_length=20,null=False)
    PetSubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    PetBreedCombination1=models.CharField(max_length=20,null=True)
    PetBreedCombination2=models.CharField(max_length=20,null=True)
    PetImage=models.FileField(upload_to="Uploads/PetImage/",null=False)
    PetCertificate=models.FileField(upload_to="Uploads/PetCertificate/",null=False)
    PetCertificateId=models.CharField(max_length=20,null=False)
    PetOwner=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Gallary(models.Model):
    GallaryImage=models.FileField(upload_to="Uploads/GallaryImage/",null=False)   
    Pet=models.ForeignKey(Pet,on_delete=models.CASCADE)

class PetDisease(models.Model):
    Disease=models.TextField(null=False)
    Pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    PetOwner=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    Date=models.DateField(auto_now=True)
    DrMessage=models.CharField(max_length=500,null=True)
    DrDesc=models.CharField(max_length=1000,null=True)
    DrDate=models.DateField(null=True)
    DrTime=models.CharField(max_length=10,null=True)
    DrMeetingCode=models.CharField(max_length=1000,null=True)
    Status=models.BooleanField(default=0)
    FeesStatus=models.BooleanField(default=0)

    class Meta: 
        ordering=["Status","Date"]

    

class BuyPet(models.Model):
    Pet=models.ForeignKey(PetSale,on_delete=models.CASCADE)
    PetOwner=models.ForeignKey(Customer,on_delete=models.CASCADE)
    No_ofPets=models.IntegerField(null=False)
    TotalPrice=models.CharField(max_length=10,null=False)
    Date=models.DateField(auto_now=True)
    DeliveryAddress=models.TextField(null=True)
    Status=models.IntegerField(default=0)


class BuyProduct(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    PetOwner=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False)
    TotalPrice=models.FloatField(null=False)
    Date=models.DateField(auto_now=True)
    DeliveryAddress=models.TextField(null=True)
    Status=models.IntegerField(default=0)

class CustomerComplaint(models.Model):
    ComplaintType=models.ForeignKey(ComplaintType,on_delete=models.SET_NULL,null=True)
    ComplaintData=models.TextField(null=False)
    Date=models.DateField(auto_now=True)
    PetOwner=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Reply=models.CharField(max_length=1000,null=True)
    Status=models.IntegerField(default=0)
