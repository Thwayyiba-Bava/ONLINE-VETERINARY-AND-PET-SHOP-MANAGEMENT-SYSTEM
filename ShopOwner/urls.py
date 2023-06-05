from ShopOwner import views
from django.urls import path,include


app_name="ShopOwners"
urlpatterns=[
     path('homepage/',views.HomePage,name="shopowner-homepage"),
     path('shopprofile/',views.ShopDetails,name="shopowner-profile"),
     path('editprofile/<int:pk>',views.ShopProfileEdit,name="shopowner-editprofile"),
     path('changepsw/<int:pk>',views.ShopPSWchange,name="shopowner-changepsw"),
     path('shopproducts/',views.ShopProducts,name="shopowner-shopproducts"),
     path('petsale/',views.PetSalesTransactions,name="shopowner-petsale"),
     path('petpurchased/',views.PetPurchased,name="shopowner-petpurchased"),
     path('proceedpetdelivery/<int:pk>/',views.ProceedPetDelivery,name="proceedPetDelivery"),
     path('pdtpurchased/',views.ProductPurchased,name="shopowner-pdtpurchased"),
     path('proceedpdtdelivery/<int:pk>/',views.ProceedProductDelivery,name="proceedProducttDelivery"),
     path('shopownerlogout/',views.ShopOwnerLogout,name="shopowner-logout"),
     path('complaints/',views.Complaints,name="shopowner-complaints"),
     path('ajax/load-productsubcategory/', views.load_productsub, name='ajax_load_pdtsubcategory'),

]