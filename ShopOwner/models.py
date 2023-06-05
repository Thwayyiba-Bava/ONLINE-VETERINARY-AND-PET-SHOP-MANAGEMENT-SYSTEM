from django.db import models

# Create your models here.
from BasicEntry.models import *
from Guest.models import *
from Guest.models import Customer


class Product(models.Model):
    ProductRate=models.FloatField(null=False)
    ProductDiscription=models.CharField(max_length=20,null=False)
    ProductPetCategory=models.ForeignKey(PetCategory,on_delete=models.SET_NULL,null=True)
    ProductProductsubCategory=models.ForeignKey(ProductsubCategory,on_delete=models.CASCADE)
    ProductImage=models.FileField(upload_to="Uploads/ProductImage/",null=False)
    ProductStock=models.IntegerField(default=0)
    Shop=models.ForeignKey(Shop,on_delete=models.CASCADE)

class PetSale(models.Model): 
    PetSaleColor=models.CharField(max_length=20,null=False)
    PetSaleGender=models.CharField(max_length=20,null=False)
    PetSaleBreed=models.CharField(max_length=20,null=False)
    PetSaleSubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    PetSaleBreedCombination1=models.CharField(max_length=20,null=True)
    PetSaleBreedCombination2=models.CharField(max_length=20,null=True)
    PetSaleImage=models.FileField(upload_to="Uploads/PetSaleImages/",null=False)
    PetSaleCertificate=models.FileField(upload_to="Uploads/PetSaleCertificates/",null=False)
    PetSaleCertificateId=models.CharField(max_length=20,null=False)
    PetSaleStock=models.IntegerField(default=0)
    PetSaleRate=models.FloatField(null=False)
    Shop=models.ForeignKey(Shop,on_delete=models.CASCADE)    


class ShopComplaint(models.Model):
    ComplaintType=models.ForeignKey(ComplaintType,on_delete=models.SET_NULL,null=True)
    ComplaintData=models.TextField(null=False)
    Date=models.DateField(auto_now=True)
    ShopOwner=models.ForeignKey(Shop,on_delete=models.CASCADE)
    Reply=models.CharField(max_length=1000,null=True)
    Status=models.IntegerField(default=0)
