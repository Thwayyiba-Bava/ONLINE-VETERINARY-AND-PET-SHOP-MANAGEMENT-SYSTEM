from django.db import models

# Create your models here.

class District(models.Model):
    District=models.CharField("District",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.District
    
class Place(models.Model):
    Place=models.CharField("Place",max_length=20,null=False,unique=True)
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.Place

class ComplaintType(models.Model):
    ComplaintType=models.CharField("ComplaintType",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.ComplaintType

class PetCategory(models.Model):
    PetCategory=models.CharField("PetCategory",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.PetCategory


class SubCategory(models.Model):
    SubCategory=models.CharField("SubCategory",max_length=20,null=False,unique=True)
    PetCategory=models.ForeignKey(PetCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.SubCategory


class Qualification(models.Model):
    Qualification=models.CharField("Qualification",max_length=20,null=False,unique=True)
    
    def __str__(self):
        return self.Qualification

class ProductCategory(models.Model):
    ProductCategory=models.CharField("ProductCategory",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.ProductCategory

class ProductsubCategory(models.Model):
    ProductCategory=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    ProductsubCategory=models.CharField("ProductsubCategory",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.ProductsubCategory
