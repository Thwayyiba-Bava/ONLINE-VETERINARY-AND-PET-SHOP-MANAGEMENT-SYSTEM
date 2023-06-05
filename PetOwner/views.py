from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Guest.models import Customer, Shop
from BasicEntry.models import *
from PetOwner.models import *
from django.contrib import messages
from Admin.models import Doctor
from ShopOwner.models import PetSale,Product
from Doctor.models import Videos


def ViewDetails(request):
    if request.session.has_key('PetOwnerid'):
        customerData=Customer.objects.get(id=request.session["PetOwnerid"])
        return render(request,"PetOwner/ViewDetails.html",{"customerData":customerData})
    else:
        return redirect('/login/') 

def EditOwnerProfile(request,pk):
    select_owner=Customer.objects.get(id=pk)

    if request.method=='POST' or request.FILES:
        select_owner.CustomerName=request.POST.get("txtName")
        select_owner.CustomerGender=request.POST.get("rdbGender")
        select_owner.CustomerContact=request.POST.get("txtPhone")
        select_owner.CustomerEmail=request.POST.get("txtEmail")
        if request.FILES:
            select_owner.CustomerImage=request.FILES.get("photo")
        select_owner.save()
        return redirect('/petowner/viewdetails/')
    else:
        return render(request,'PetOwner/EditProfile.html',{'owner':select_owner})

def ChangeOwnerPSW(request,pk):
    select_owner=Customer.objects.get(id=pk)
    psw=select_owner.CustomerPassword
    if request.method=='POST':
        old=request.POST.get("Oldpass")
        if old != psw :
            error="Old password is not correct"
            return render(request,"PetOwner/ChangeOwnerPSW.html",{'error':error})
        else:
            newpass=request.POST.get("Newpass")
            select_owner.CustomerPassword=newpass
            select_owner.save()
            messages.success(request,'Password Changed Successfully.Please Login!')
            return redirect("/login/")
    else:
        return render(request,'PetOwner/ChangeOwnerPSW.html')


        
def load_subcategory(request):
    petcategory_id = request.GET.get('petcategory')
    subcategory = SubCategory.objects.filter(PetCategory=petcategory_id)
    return render(request, 'PetOwner/subcategory_dropdown_list.html', {'subcategory': subcategory})
    


def ManagePets(request):
    if "PetOwnerid" in request.session:
        allsubcategory=SubCategory.objects.all()
        allpetcategory=PetCategory.objects.all()
        
        petObj=Pet() 
        ownerobj=Customer.objects.get(id=request.session["PetOwnerid"])

        if request.method=="POST" and request.FILES:
            
            petObj.PetGender=request.POST.get("rdbgender")
            x=request.POST.get("slctColor")
            if x=='Other':
                petObj.Petcolor=request.POST.get("color")
            else:
                petObj.Petcolor=x
            petObj.PetBreed=request.POST.get("rdbBreed")
            petObj.PetBreedCombination1=request.POST.get("txtBC1")
            petObj.PetBreedCombination2=request.POST.get("txtBC2")
            subcategoryObj=SubCategory.objects.get(id=request.POST.get("slctSubCategory")) 
            petObj.PetSubCategory=subcategoryObj
            petObj.PetImage=request.FILES.get("flImage")
            petObj.PetCertificate=request.FILES.get("flCertificate")
            petObj.PetCertificateId=request.POST.get("txtId")
            
            petObj.PetOwner=ownerobj
            petObj.save()
      
            
            pet=Pet.objects.all().filter(PetOwner=request.session["PetOwnerid"])
            return render(request,"PetOwner/ManagePets.html",{"petSubCategory":allsubcategory,"petCategory":allpetcategory,"pet":pet})
        else:
            pet=Pet.objects.all().filter(PetOwner=request.session["PetOwnerid"])
            return render(request,"PetOwner/ManagePets.html",{"petSubCategory":allsubcategory,"petCategory":allpetcategory,"pet":pet})
    else:
        return redirect('/login/')         

def PetGallary(request,pk):
    gallaryObj=Gallary()
    pet=Pet.objects.get(id=pk)
    if request.method=="POST"and request.FILES:
        gallaryObj.GallaryImage=request.FILES.get("filename") 
        gallaryObj.Pet=pet
        gallaryObj.save()
        
        gallary=Gallary.objects.all().filter(Pet=pk)    
        return render(request,"PetOwner/PetGallary.html",{"gallary":gallary})
    else:
        gallary=Gallary.objects.all().filter(Pet=pk)      
        return render(request,"PetOwner/PetGallary.html",{"gallary":gallary})   

def SearchPets(request):
    petData=PetCategory.objects.all()
    subData=SubCategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("slctpetsub")
        pets=PetSale.objects.filter(PetSaleSubCategory=subcategory)  

        return render(request,"PetOwner/SearchPets.html",{"categoryData":petData,"cateData":subData,'pets':pets})
    else:
        return render(request,"PetOwner/SearchPets.html",{"categoryData":petData,"cateData":subData})

def ViewPetDetails(request,pk):
    pet=PetSale.objects.get(id=pk)
    return render(request,'PetOwner/PetDetails.html',{'pet':pet})


def SearchDoctor(request):
    district=District.objects.all()
    if request.method == 'POST':
        dist=request.POST.get('slctDistrict')
        doctors=Doctor.objects.filter(District=dist)
        return render(request,'PetOwner/SearchDoctor.html',{'district':district,'doctors':doctors})
    else:
        return render(request,'PetOwner/SearchDoctor.html',{'district':district})
    
def BuythePet(request,pk):
    pet=PetSale.objects.get(id=pk)
    ownerobj=Customer.objects.get(id=request.session["PetOwnerid"])
    if request.method=='POST':
        BuyPet.objects.create(Pet=pet,PetOwner=ownerobj,No_ofPets=request.POST.get('petnumber'),
                                TotalPrice=request.POST.get('total'),DeliveryAddress=request.POST.get("deladdress"))
        quantity=request.POST.get('petnumber')
        stock=pet.PetSaleStock
        stock=int(stock)-int(quantity)
        pet.PetSaleStock=stock
        pet.save()
        return redirect('/petowner/SearchPets/')
    else:
        return render(request,'PetOwner/BuyPet.html',{'pet':pet})

def MedicalTips(request):
    videos=Videos.objects.all().order_by('-VideoDate')
    return render(request,'PetOwner/MedicalTips.html',{'videos':videos})

def ContactDoctor(request,pk):
    doctor=Doctor.objects.get(id=pk)
    pets=Pet.objects.filter(PetOwner=request.session["PetOwnerid"])
    if request.method=='POST':
        petowner=Customer.objects.get(id=request.session["PetOwnerid"])
        pet=request.POST.get('slctPetCategory')
        petcat=Pet.objects.get(id=pet)
        PetDisease.objects.create(Disease=request.POST.get('issue'),Pet=petcat,
                                PetOwner=petowner,Doctor=doctor)
        
        return redirect('/petowner/DrFees/')

        
    else:
        return render(request,'PetOwner/ContactDoctor.html',{'doctor':doctor,'pets':pets})

def DrFees(request):
    if request.method=='POST':
        ds=PetDisease.objects.last()
        ds.FeesStatus=1                               #check
        ds.save()
        return redirect('/petowner/Mypetissues/')
    else:
        return render(request,'PetOwner/DrFees.html')




def SearchProducts(request):
    prdtData=ProductCategory.objects.all()
    pdtsubData=ProductsubCategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("slctpdtsub")
        pdts=Product.objects.filter(ProductProductsubCategory=subcategory)  

        return render(request,"PetOwner/SearchProduct.html",{"categoryData":prdtData,"cateData":pdtsubData,'pdts':pdts})
    else:
        return render(request,"PetOwner/SearchProduct.html",{"categoryData":prdtData,"cateData":pdtsubData})


def buyProduct(request,pk):
    pdt=Product.objects.get(id=pk)
    ownerobj=Customer.objects.get(id=request.session["PetOwnerid"])
    if request.method=='POST':
        BuyProduct.objects.create(Product=pdt,PetOwner=ownerobj,quantity=request.POST.get('pdtnumber'),
                                    TotalPrice=request.POST.get('total'),DeliveryAddress=request.POST.get("deladdress"))
        quant=request.POST.get('pdtnumber')
        stock=pdt.ProductStock
        stock=int(stock)-int(quant)
        pdt.ProductStock=stock
        pdt.save()
        return redirect('/petowner/SearchProducts/')
    else:
        return render(request,'PetOwner/BuyProduct.html',{'pdt':pdt})

def PetOwnerLogout(request):
    if "PetOwnerid" in request.session:
        del request.session["PetOwnerid"]
    return redirect('/login/')

def PetOrders(request):
    orders=BuyPet.objects.filter(PetOwner=request.session["PetOwnerid"])
    return render(request,'PetOwner/MyPetOrders.html',{'orders':orders})

def ProductOrders(request):
    orders=BuyProduct.objects.filter(PetOwner=request.session["PetOwnerid"])
    return render(request,'PetOwner/MyProductOrders.html',{'orders':orders})

def CustomerComplaints(request):
    compltypes=ComplaintType.objects.all()
    petowner=Customer.objects.get(id=request.session['PetOwnerid'])
    if request.method=='POST':
        type=request.POST.get('compltype')
        compltp=ComplaintType.objects.get(id=type)
        CustomerComplaint.objects.create(ComplaintType=compltp,ComplaintData=request.POST.get('complaint'),PetOwner=petowner)

        complaints=CustomerComplaint.objects.filter(PetOwner=petowner)
        return render(request,'PetOwner/CustomerComplaints.html',{'compltypes':compltypes,'complaints':complaints})
    else:
        complaints=CustomerComplaint.objects.filter(PetOwner=petowner)
        return render(request,'PetOwner/CustomerComplaints.html',{'compltypes':compltypes,'complaints':complaints})

def ProceedPetDelivery(request,pk):
    petpurchase=BuyPet.objects.get(id=pk)
    petpurchase.Status=2
    petpurchase.save()
    return redirect('/petowner/Mypetorders/')

def ProceedProductDelivery(request,pk):
    pdtpurchase=BuyProduct.objects.get(id=pk)
    pdtpurchase.Status=2
    pdtpurchase.save()
    return redirect('/petowner/Myproductorders/')

def MyPetIssues(request):
    issues=PetDisease.objects.filter(PetOwner=request.session['PetOwnerid'])
    return render(request,'PetOwner/MyPetIssues.html',{'issues':issues})

def DrMessage(request,pk):
    issue=PetDisease.objects.get(id=pk)
    return render(request,'PetOwner/DrReply.html',{'issue':issue})
