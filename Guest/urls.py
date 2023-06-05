from Guest import views
from django.urls import path,include

app_name="Guest"
urlpatterns=[
    path('newuser/',views.NewUser,name="newuser-signup"),
    path('newshop/',views.NewShop,name="newshop-signup"),
    path('login/',views.Login,name="login"),
    path('ajax/load-places/', views.load_places, name='ajax_load_places'),
    path('',views.Home,name="home"),
   
]
