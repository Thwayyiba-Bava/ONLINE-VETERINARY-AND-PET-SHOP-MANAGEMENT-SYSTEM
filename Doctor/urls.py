from Doctor import views
from django.urls import path,include


app_name="Doctor"
urlpatterns=[
    path('homepage/',views.HomePage,name="doctor-homepage"),
    path('viewdetails/',views.viewdetails,name="doctor-viewdetails"),
    path('medicalvideos/',views.MedicalVideos,name="doctor-medicalvideos"),
    path('petissues/',views.PetIssues,name="pet-issues"),
    path('petissuereply/<int:pk>/',views.PetIssueReply,name="Petissuereply"),
    path('doctorlogout/',views.DoctorLogout,name="doctor-logout"),
    path('editdoctorprofile/<int:pk>/',views.EditDoctorProfile,name="edit-doctorprofile"),
    path('changedoctorpsw/<int:pk>/',views.ChangeDoctorPassword,name="change-doctorpassword"),

]