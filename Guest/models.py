from django.db import models

# Create your models here.
from BasicEntry.models import Place


class Customer(models.Model):
    CustomerName=models.CharField(max_length=20,null=False)
    CustomerGender=models.CharField(max_length=20,null=False)
    CustomerContact=models.CharField(max_length=20,null=False)
    CustomerEmail=models.EmailField(max_length=20,null=False,unique=True)
    CustomerPlace=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    CustomerImage=models.FileField(upload_to='Uploads/PetOwnerPhotos/',null=True)
    CustomerUsername=models.CharField(max_length=20,null=False)
    CustomerPassword=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.CustomerName
        
class Shop(models.Model):
    ShopName=models.CharField(max_length=20,null=False)
    ShopContact=models.CharField(max_length=20,null=False)
    ShopEmail=models.CharField(max_length=20,null=False)
    ShopPlace=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    ShopLicencenumber=models.CharField(max_length=20,null=False)
    ShopProof=models.FileField(upload_to='Uploads/ShopProof/',null=False)
    ShopUsername=models.CharField(max_length=20,null=False)
    ShopPassword=models.CharField(max_length=20,null=False)
    shopStatus=models.BooleanField(default=False)

