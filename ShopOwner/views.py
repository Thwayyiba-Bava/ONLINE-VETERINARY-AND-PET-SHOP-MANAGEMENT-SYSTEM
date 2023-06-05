from django.shortcuts import render,redirect
from BasicEntry.models import ComplaintType, PetCategory,ProductCategory,ProductsubCategory,SubCategory,PetCategory
import ShopOwner
from ShopOwner.models import Product,PetSale, ShopComplaint
from PetOwner.models import BuyProduct,BuyPet
from Guest.models import Customer, Shop
from django.contrib import messages


def HomePage(request):
    if request.session.has_key('Shopownerid'):
        return render(request,"ShopOwner/HomePage.html",{})
    else:
        return redirect("Guest:login")

def ShopDetails(request):
    if request.session.has_key('Shopownerid'):
        shopdata=Shop.objects.get(id=request.session["Shopownerid"])
        return render(request,"ShopOwner/ShopProfile.html",{"shopdata":shopdata})
    else:
        return redirect("Guest:login")

def ShopProfileEdit(request,pk):
    select_shop=Shop.objects.get(id=pk)

    if request.method=='POST' or request.FILES:
        select_shop.ShopName=request.POST.get("txtName")
        
        select_shop.ShopContact=request.POST.get("txtPhone")
        select_shop.ShopEmail=request.POST.get("txtEmail")
        select_shop.ShopLicencenumber=request.POST.get("txtlcnsnum")
        if request.FILES:
            select_shop.ShopProof=request.FILES.get("filename")
        select_shop.save()
        return redirect('/shopowner/shopprofile/')
    else:
        return render(request,'ShopOwner/EditShopProfile.html',{'shop':select_shop})


def ShopPSWchange(request,pk):
    select_shop=Shop.objects.get(id=pk)
    psw=select_shop.ShopPassword
    if request.method=='POST':
        old=request.POST.get("Oldpass")
        if old != psw :
            error="Old password is not correct"
            return render(request,"ShopOwner/ChangeShopPSW.html",{'error':error})
        else:
            newpass=request.POST.get("Newpass")
            select_shop.ShopPassword=newpass
            select_shop.save()
            messages.success(request,'Password Changed Successfully.Please Login!')
            return redirect("/login/")
    else:
        return render(request,'ShopOwner/ChangeShopPSW.html')



def ShopProducts(request):
    if "Shopownerid" in request.session:
        allpetcategory=PetCategory.objects.all()
        allproductcategory=ProductCategory.objects.all()
        allproductsubcategory=ProductsubCategory.objects.all()
        productObj=Product() 

        if request.method=="POST" and request.FILES:
            petcategoryObj=PetCategory.objects.get(id=request.POST.get("slctPetCategory")) 
            productObj.ProductPetCategory=petcategoryObj
            
            productsubcategoryObj=ProductsubCategory.objects.get(id=request.POST.get("slctproductsub")) 
            productObj.ProductProductsubCategory=productsubcategoryObj
            
            productObj.ProductRate=request.POST.get("rate")
            productObj.ProductStock=request.POST.get("stock")
            productObj.ProductImage=request.FILES.get("flImage")
            productObj.ProductDiscription=request.POST.get("discription")

            shop=Shop.objects.get(id=request.session['Shopownerid'])
            productObj.Shop=shop
            productObj.save()

            product=Product.objects.all().filter(Shop=request.session['Shopownerid'])
            return render(request,"ShopOwner/ShopProducts.html",{"categoryData":allpetcategory,"catData":allproductcategory,"cateData":allproductsubcategory,"videos":product})
        else:
            product=Product.objects.all().filter(Shop=request.session['Shopownerid'])
            return render(request,"ShopOwner/ShopProducts.html",{"categoryData":allpetcategory,"catData":allproductcategory,"cateData":allproductsubcategory,"videos":product})
    else:
        return redirect('guest/login/')

def PetSalesTransactions(request):
    if "Shopownerid" in request.session:
        allsubcategory=SubCategory.objects.all()
        allpetcategory=PetCategory.objects.all()
        petsaleObj=PetSale() 
       

        if request.method=="POST" and request.FILES:
            
            petsaleObj.PetSaleGender=request.POST.get("rdbgender")
            x=request.POST.get("slctColor")
            if x=='Other':
                petsaleObj.PetSaleColor=request.POST.get("color")
            else:
                petsaleObj.PetSaleColor=x
            petsaleObj.PetSaleBreed=request.POST.get("rdbBreed")
            petsaleObj.PetSaleBreedCombination1=request.POST.get("txtBC1")
            petsaleObj.PetSaleBreedCombination2=request.POST.get("txtBC2")
            subcategoryObj=SubCategory.objects.get(id=request.POST.get("slctSubCategory")) 
            petsaleObj.PetSaleSubCategory=subcategoryObj
            petsaleObj.PetSaleImage=request.FILES.get("flImage")
            petsaleObj.PetSaleCertificate=request.FILES.get("flCertificate")
            petsaleObj.PetSaleCertificateId=request.POST.get("txtId")
            petsaleObj.PetSaleStock=request.POST.get("txtStok")
            petsaleObj.PetSaleRate=request.POST.get("txtprice")
            shop=Shop.objects.get(id=request.session['Shopownerid'])
            petsaleObj.Shop=shop
            petsaleObj.save()
      
            
            petsale=PetSale.objects.all().filter(Shop=request.session['Shopownerid'])
            return render(request,"ShopOwner/PetSale.html",{"petSubCategory":allsubcategory,"petCategory":allpetcategory,"pet":petsale})
        else:
            petsale=PetSale.objects.all().filter(Shop=request.session['Shopownerid'])
            return render(request,"ShopOwner/PetSale.html",{"petSubCategory":allsubcategory,"petCategory":allpetcategory,"pet":petsale})
    else:
        return redirect('/login/')         

def PetPurchased(request):
    petpurchase=BuyPet.objects.filter(Pet__Shop=request.session['Shopownerid'])
    return render(request,"ShopOwner/PurchasedPet.html",{'petpurchase':petpurchase})

def ProceedPetDelivery(request,pk):
    petpurchase=BuyPet.objects.get(id=pk)
    petpurchase.Status=1
    petpurchase.save()
    return redirect('/shopowner/petpurchased/')


def ShopOwnerLogout(request):
    if "Shopownerid" in request.session:
        del request.session["Shopownerid"]
    return redirect('/login/')

def load_productsub(request):
    product_id = request.GET.get('product')
    productsub = ProductsubCategory.objects.filter(ProductCategory=product_id)
    return render(request, 'ShopOwner/ProductSubcategory_dropdown_list.html', {'productsub': productsub})

def ProductPurchased(request):
    pdtpurchase=BuyProduct.objects.filter(Product__Shop=request.session['Shopownerid'])
    return render(request,"ShopOwner/PurchasedProduct.html",{'pdtpurchase':pdtpurchase})

def ProceedProductDelivery(request,pk):
    pdtpurchase=BuyProduct.objects.get(id=pk)
    pdtpurchase.Status=1
    pdtpurchase.save()
    return redirect('/shopowner/pdtpurchased/')

def Complaints(request):
    compltypes=ComplaintType.objects.all()
    shopowner=Shop.objects.get(id=request.session['Shopownerid'])
    if request.method=='POST':
        type=request.POST.get('compltype')
        compltp=ComplaintType.objects.get(id=type)
        ShopComplaint.objects.create(ComplaintType=compltp,ComplaintData=request.POST.get('complaint'),ShopOwner=shopowner)

        complaints=ShopComplaint.objects.filter(ShopOwner=shopowner)
        return render(request,'ShopOwner/Complaints.html',{'compltypes':compltypes,'complaints':complaints})
    else:
        complaints=ShopComplaint.objects.filter(ShopOwner=shopowner)
        return render(request,'ShopOwner/Complaints.html',{'compltypes':compltypes,'complaints':complaints})
