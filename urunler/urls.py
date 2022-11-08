from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('detay/<int:id>',detay,name='detay'),
    path('sepet/',sepet,name='sepet'),
    path('checkout/',checkout,name='checkout'),
    path('siparisler/',siparisler,name='siparisler'),
    path('checkout/',checkout,name='checkout'),
    path('adres/',adres,name='adres'),
    
]
