from django.shortcuts import render,redirect

from BasicEntry.models import District, Qualification
from Admin.models import Doctor, DrQualification
from Guest.models import Shop
from PetOwner.models import *
from django.http import HttpResponse

from ShopOwner.models import ShopComplaint

# Create your views here.

def ManageDoctors(request):
    alldistrict=District.objects.all()
    doctorObj=Doctor()
    qual=Qualification.objects.all()

    if request.method=="POST" and request.FILES:
        distid=request.POST.get("slctDistrict")
        district=District.objects.get(id=distid)

        doctorObj.District=district
        doctorObj.DoctorName=request.POST.get("txtName")
        doctorObj.DoctorGender=request.POST.get("rdbGender")
        doctorObj.DoctorContact=request.POST.get("txtPhone")
        doctorObj.DoctorEmail=request.POST.get("txtEmail")
        doctorObj.HospitalAddress=request.POST.get("address")
        doctorObj.DoctorPhoto=request.FILES.get("flImage")
        doctorObj.QualCertificate=request.FILES.get("qualcertf")
        doctorObj.DoctorUsername=request.POST.get("txtUsername")
        doctorObj.DoctorPassword=request.POST.get("txtPassword")
        doctorObj.save()

        qualf=request.POST.getlist('qualf')
        dr=Doctor.objects.last()
        for data in qualf:
            qualobj=Qualification.objects.get(id=data)
            DrQualification.objects.create(Doctor=dr,Qualification=qualobj)

        doctor=Doctor.objects.all()
       
        return render(request,"Admin/ManageDoctors.html",{"doctor":doctor,"disData":alldistrict,'qual':qual})
    else:
        doctor=Doctor.objects.all()
        return render(request,"Admin/ManageDoctors.html",{"disData":alldistrict,'qual':qual,"doctor":doctor})

    
        
def DeleteDoctor(request,pk):
    dr=Doctor.objects.get(id=pk)
    dr.delete()
    return redirect('/admin1/ManageDoctors/')
    
    
def ManageShops(request):
    shops=Shop.objects.all()
    return render(request,"Admin/ShopVerification.html",{'shops':shops})  

def ApproveShops(request,pk):
    shop=Shop.objects.get(id=pk)
    shop.shopStatus=True
    shop.save()
    return redirect('/admin1/ManageShops/')

def RejectShops(request,pk):
    shop=Shop.objects.get(id=pk)
    shop.shopStatus=False
    shop.save()
    return redirect('/admin1/ManageShops/')


def PetPurchased(request):
    petpurchase=BuyPet.objects.all()
    return render(request,"Admin/PurchasedPets.html",{'petpurchase':petpurchase})



def ProductPurchased(request):
    pdtpurchase=BuyProduct.objects.all()
    return render(request,"Admin/PurchasedProducts.html",{'pdtpurchase':pdtpurchase})




def PetOwnerComplaints(request):
    compl=CustomerComplaint.objects.all()
    return render(request,'Admin/CustomerComplaints.html',{'complaints':compl})

def CustomerComplReply(request,pk):
    compl=CustomerComplaint.objects.get(id=pk)
    if request.method=='POST':
        compl.Reply=request.POST.get('reply')
        compl.Status=1
        compl.save()
        return redirect('/admin1/customercomplaint/')
    else:
        return render(request,'Admin/ComplaintReply.html')

def ShopComplaints(request):
    compl=ShopComplaint.objects.all()
    return render(request,'Admin/ShopComplaints.html',{'complaints':compl})

def ShopComplReply(request,pk):
    compl=ShopComplaint.objects.get(id=pk)
    if request.method=='POST':
        compl.Reply=request.POST.get('reply')
        compl.Status=1
        compl.save()
        return redirect('/admin1/shopcomplaint/')
    else:
        return render(request,'Admin/ComplaintReply.html')

def AdminLogout(request):
    return redirect('/login/')