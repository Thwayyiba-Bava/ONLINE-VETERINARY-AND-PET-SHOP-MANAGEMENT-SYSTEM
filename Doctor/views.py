from django.shortcuts import render,redirect
from Admin.models import Doctor,DrQualification
from BasicEntry.models import Qualification
from Doctor.models import Videos
from PetOwner.models import PetDisease
import datetime
from django.contrib import messages

# Create your views here.
def HomePage(request):
    if "Doctorid" in request.session:
        return render(request,"Doctor/HomePage.html",{})
    else:
       return redirect('/login/') 

def viewdetails(request):
    if request.session.has_key('Doctorid'):
        dr=Doctor.objects.get(id=request.session['Doctorid'])
        return render(request,"Doctor/viewdetails.html",{'doctor':dr}) 
    else:
        return redirect('/login/')

def MedicalVideos(request):
    if "Doctorid" in request.session:
        videosObj=Videos() 
        docobj=Doctor.objects.get(id=request.session["Doctorid"])
        
        if request.method=="POST" and request.FILES:
            videosObj.VideosCaption=request.POST.get("txtCaption")
            videosObj.VideosDescription=request.POST.get("txtDis")
            videosObj.VideosVideo=request.FILES.get("flVideo")
            videosObj.Doctor=docobj
            videosObj.save()

            videos=Videos.objects.all().filter(Doctor=docobj.id).order_by('-VideoDate')
            return render(request,"Doctor/MedicalVideos.html",{"videos":videos})
        else:
            videos=Videos.objects.all().filter(Doctor=docobj.id).order_by('-VideoDate')
            return render(request,"Doctor/MedicalVideos.html",{"videos":videos})  
    else:       
        return redirect('/login/')
            
def DoctorLogout(request):
    if "Doctorid" in request.session:
        del request.session["Doctorid"]
    return redirect('/login/')

def EditDoctorProfile(request,pk):
    select_doctor=Doctor.objects.get(id=pk)
    qual=Qualification.objects.all()
    qualf=DrQualification.objects.filter(Doctor=pk)
    if request.method=='POST' or request.FILES:
        select_doctor.DoctorName=request.POST.get("txtName")
        select_doctor.DoctorGender=request.POST.get("rdbGender")
        select_doctor.DoctorContact=request.POST.get("txtPhone")
        select_doctor.DoctorEmail=request.POST.get("txtEmail")
        select_doctor.HospitalAddress=request.POST.get("address")
        qualf1=request.POST.getlist('qualf')
        qualf.delete()
        
        for data in qualf1:
            qualobj=Qualification.objects.get(id=data)
            DrQualification.objects.create(Doctor=select_doctor,Qualification=qualobj)
            

        if request.FILES:
            if request.FILES.get("flImage"):
                select_doctor.DoctorPhoto=request.FILES.get("flImage")
            if request.FILES.get("qualcertf"):
                select_doctor.QualCertificate=request.FILES.get("qualcertf")

        select_doctor.save()
        return redirect('/doctor/viewdetails/')
    else:
        return render(request,'Doctor/EditDoctorProfile.html',{'doctor':select_doctor,'qual':qual,'qualf':qualf})
        

def ChangeDoctorPassword(request,pk):
    select_doctor=Doctor.objects.get(id=pk)
    psw=select_doctor.DoctorPassword
    if request.method=='POST':
        old=request.POST.get("Oldpass")
        if old != psw :
            error="Old password is not correct"
            return render(request,"Doctor/ChangeDoctorPSW.html",{'error':error})
        else:
            newpass=request.POST.get("Newpass")
            select_doctor.DoctorPassword=newpass
            select_doctor.save()
            messages.success(request,'Password Changed Successfully.Please Login!')
            return redirect("/login/")
    else:
        return render(request,'Doctor/ChangeDoctorPSW.html')

def PetIssues(request):
    if "Doctorid" in request.session:
        issues=PetDisease.objects.filter(Doctor=request.session['Doctorid'])
        return render(request,"Doctor/PetIssues.html",{'issues':issues})
    else:
        return redirect("/login/")

def PetIssueReply(request,pk):
    issue=PetDisease.objects.get(id=pk)
    if request.method=='POST':
        issue.DrMessage=request.POST.get('message')
        issue.DrDesc=request.POST.get('desc')
        issue.DrDate=request.POST.get('txtdate')
        issue.DrTime=request.POST.get('txttime')
        issue.DrMeetingCode=request.POST.get('meetcode')
        issue.Status=True
        issue.save()
        return redirect("/doctor/petissues/") 
    else:
        return render(request,"Doctor/PetIssueReply.html")


       