from Admin import views
from django.urls import path,include

app_name="Admin"
urlpatterns=[
    path('ManageDoctors/',views.ManageDoctors,name="admin-managedoctors"),
    path('Deletedoctor/<int:pk>/',views.DeleteDoctor,name="delete-doctor"),
    path('ManageShops/',views.ManageShops,name="manage-shops"),
    path('ApproveShops/<int:pk>',views.ApproveShops,name="approve-shop"),
    path('RejectShops/<int:pk>',views.RejectShops,name="reject-shop"),

    path('petpurchased/',views.PetPurchased,name="pet-purchased"),
    
    path('pdtpurchased/',views.ProductPurchased,name="product-purchased"),
    
    path('customercomplaint/',views.PetOwnerComplaints,name="customer-complaint"),
    path('customercomplaintreply/<int:pk>/',views.CustomerComplReply,name="customer-complaint-reply"),
    path('shopcomplaint/',views.ShopComplaints,name="shop-complaint"),
    path('shopcomplaintreply/<int:pk>/',views.ShopComplReply,name="shop-complaint-reply"),
    path('Logout/',views.AdminLogout,name="admin-logout"),
]