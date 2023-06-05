from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from Guest.models import Customer
from BasicEntry.models import Place,District
from Guest.models import Shop
from Admin.models import AdminRegister, Doctor


def load_places(request):
    district_id = request.GET.get('district')
    places = Place.objects.filter(District=district_id)
    return render(request, 'Guest/Place_dropdown_list.html', {'places': places})

def NewUser(request):

    allplace=Place.objects.all()
    
    alldistrict=District.objects.all()
    customerObj=Customer() #Object Creation

    if request.method=="POST" and request.FILES:
        customerObj.CustomerName=request.POST.get("txtName")
        customerObj.CustomerGender=request.POST.get("rdbGender")
        customerObj.CustomerContact=request.POST.get("txtPhone")
        customerObj.CustomerEmail=request.POST.get("txtEmail")
        placeObj=Place.objects.get(id=request.POST.get("slctPlace")) #Get Place Object
        customerObj.CustomerPlace=placeObj
        customerObj.CustomerImage=request.FILES.get("photo")
        customerObj.CustomerUsername=request.POST.get("txtUsername")
        customerObj.CustomerPassword=request.POST.get("txtPassword")
        customerObj.save()
        return redirect('/login/')
    else:
        return render(request,"Guest/NewUser.html",{"placData":allplace,"distData":alldistrict})


def NewShop(request):

    allplace=Place.objects.all()
    print(allplace)
    alldistrict=District.objects.all()
    shopObj=Shop() #Object Creation

    if request.method=="POST" and request.FILES:
        shopObj.ShopName=request.POST.get("txtName")
        shopObj.ShopContact=request.POST.get("txtPhone")
        shopObj.ShopEmail=request.POST.get("txtEmail")
        placeObj=Place.objects.get(id=request.POST.get("slctPlace")) #Get Place Object
        shopObj.ShopPlace=placeObj
        shopObj.ShopLicencenumber=request.POST.get("txtlcnsnum")
        shopObj.ShopProof=request.FILES.get("filename")
        shopObj.ShopUsername=request.POST.get("txtUsername")
        shopObj.ShopPassword=request.POST.get("txtPassword")
        shopObj.save()
        return redirect('/login/')
    else:
        return render(request,"Guest/NewShop.html",{"placData":allplace,"distData":alldistrict})


def Login(request):
    if request.method=="POST":
        petownercount=Customer.objects.filter(CustomerUsername=request.POST.get("txtUsername"),CustomerPassword=request.POST.get("txtPassword")).count()
        shopownercount=Shop.objects.filter(ShopUsername=request.POST.get("txtUsername"),ShopPassword=request.POST.get("txtPassword")).count()
        doctorcount=Doctor.objects.filter(DoctorUsername=request.POST.get("txtUsername"),DoctorPassword=request.POST.get("txtPassword")).count()
        admincount=AdminRegister.objects.filter(Username=request.POST.get("txtUsername"),Password=request.POST.get("txtPassword")).count()

        if admincount>0:
            return redirect("/admin1/ManageDoctors/")

        if petownercount>0:
            print("Pet Count",petownercount)
            petownerobj=get_object_or_404(Customer,CustomerUsername=request.POST.get("txtUsername"),CustomerPassword=request.POST.get("txtPassword"))
            request.session["PetOwnerid"]=petownerobj.id
            return redirect("PetOwner:petowner-viewdetails")

        if doctorcount>0:
            print("Doctor Count",doctorcount)
            doctorobj=get_object_or_404(Doctor,DoctorUsername=request.POST.get("txtUsername"),DoctorPassword=request.POST.get("txtPassword"))
            request.session["Doctorid"]=doctorobj.id
            return redirect("Doctor:doctor-viewdetails")   

        elif shopownercount>0:
            shopownerobj=get_object_or_404(Shop,ShopUsername=request.POST.get("txtUsername"),ShopPassword=request.POST.get("txtPassword"))
            if shopownerobj.shopStatus==True:
                request.session["Shopownerid"]=shopownerobj.id
                return redirect("ShopOwners:shopowner-profile")
            else:
                return redirect('/login/')
        else:
            err='Username or Password is incorrect'
            return render(request,"Guest/Login.html",{'err':err})
    else:
        return render(request,"Guest/Login.html",{})


def Home(request):
    return render(request,'Guest/LandingPage.html')


    