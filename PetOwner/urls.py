from PetOwner import views
from django.urls import path,include


app_name="PetOwner"
urlpatterns=[
    
    path('viewdetails/',views.ViewDetails,name="petowner-viewdetails"),
    path('editprofile/<int:pk>/',views.EditOwnerProfile,name="petowner-editprofile"),
    path('changepsw/<int:pk>/',views.ChangeOwnerPSW,name="petowner-changepsw"),
    path('ManagePets/',views.ManagePets,name="petowner-managepets"),
    path('PetGallary/<int:pk>',views.PetGallary,name="petowner-petgallary"),
    path('SearchPets/',views.SearchPets,name="petowner-searchpets"),
    path('SearchProducts/',views.SearchProducts,name="petowner-searchproducts"),
    path('viewpetdetails/<int:pk>/',views.ViewPetDetails,name="ViewPetDetails"),
    path('buythepet/<int:pk>/',views.BuythePet,name="Buypet"),
    path('buyproduct/<int:pk>/',views.buyProduct,name="BuyProducts"),
    path('SearchDoctor/',views.SearchDoctor,name="petowner-searchdoctor"),
    path('MedicalTips/',views.MedicalTips,name="petowner-medicaltips"),
    path('ContactDoctor/<int:pk>/',views.ContactDoctor,name="contact-doctor"),
    path('PetownerLogout/',views.PetOwnerLogout,name="petowner-logout"),
    path('ajax/load-subcategory/',views.load_subcategory, name='ajax_load_subcategory'),
    path('Mypetorders/',views.PetOrders,name="petowner-petorders"),
    path('Myproductorders/',views.ProductOrders,name="petowner-productorders"),
    path('Complaints/',views.CustomerComplaints,name="petowner-complaints"),
    path('Mypetissues/',views.MyPetIssues,name="petowner-petissues"),
    path('DrMessage/<int:pk>',views.DrMessage,name="Drmessage"),
    path('DrFees/',views.DrFees,name="Drfees"),
    path('proceedpetdelivery/<int:pk>/',views.ProceedPetDelivery,name="proceedPetDelivery"),
    path('proceedpdtdelivery/<int:pk>/',views.ProceedProductDelivery,name="proceedProducttDelivery"),
]