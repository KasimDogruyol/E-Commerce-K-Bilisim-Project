from django.urls import path
from .views import *

urlpatterns = [
    path('register/',userRegister,name='register'),
    path('login/',userLogin,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('order_details/',order_details,name='order_details'),
    path('profil/',profil,name='profil'),
    path('sifredegistir/',sifredegistir,name='sifredegistir'),
]
