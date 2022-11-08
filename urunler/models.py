from django.db import models
from django.conf import settings
from user.views import *
from django.contrib.auth.models import User
# Create your models here.
from django.forms import ModelForm
class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    foto = models.FileField(upload_to='images/kategoriler', null=True, blank=True)
    def __str__(self):
        return self.isim
class KategoriFotograflari(models.Model):
    kategori = models.ForeignKey(Kategori,on_delete=models.CASCADE)
    foto = models.FileField(upload_to='images/kategoriler')
    def __str__(self):
        return self.kategori.isim
    
class Subcategory(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim
class SeriNo(models.Model):
    no = models.CharField(max_length= 50)
    def __str__(self):
        return self.no
class Urun(models.Model):
    kategori = models.ForeignKey(Kategori,on_delete=models.CASCADE,null = True)
    subcategories = models.ManyToManyField(Subcategory)
    no = models.OneToOneField(SeriNo,on_delete=models.SET_NULL,null = True)
    urun_adi = models.CharField(max_length=100,null = True,blank = True)
    urun_aciklama = models.CharField(max_length=100,null = True,blank = True)
    urun_fiyat = models.IntegerField(null = True,blank = True)
    urun_ekipman = models.CharField(max_length=100,null = True,blank = True)
    urun_marka = models.CharField(max_length=100,null = True,blank = True)
    resim = models.FileField(upload_to='urunler/',null = True,blank = True)
    urun_firma = models.CharField(max_length=100,null = True,blank = True)
    adet = models.IntegerField(null = True,blank = True, default=1)
    def __str__(self):
        return self.urun_adi
    
    

class Sepet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    urunler = models.ForeignKey(Urun, on_delete=models.CASCADE, null=True)
    adet = models.IntegerField(null = True,blank = True)
    fiyat = models.IntegerField(null = True,blank = True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    # @property
    # def fiyat(self):
    #     return (self.urun.urun_fiyat)
    # @property
    # def tutar(self):
    #     return (self.adet * self.urun.urun_fiyat)

# class ShopCart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
#     urun = models.ForeignKey(Urun,on_delete=models.CASCADE,null = True)
#     urunler = models.ManyToManyField(Urun)
#     quantity = models.IntegerField(null = True,blank = True)
#     def __str__(self):
#         return self.user.username
#     @property
#     def fiyat(self):
#         return (self.urun.urun_fiyat)
#     @property
#     def tutar(self):
#         return (self.quantity * self.urun.urun_fiyat)
# class ShopCartForm(ModelForm):
#     class Meta:
#         model = ShopCart
#         fields = ['quantity']
class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Prepared','Prepared'),
        ('OnShipping','OnShipping'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    tel = models.IntegerField(null = True,blank = True)
    adres = models.CharField(blank=True,max_length=150)
    sehir = models.CharField(blank=True,max_length=20)
    ilce = models.CharField(blank=True,max_length=20)
    posta = models.CharField(blank=True,max_length=20)
    kartisim = models.CharField(null=True,blank=True,max_length=20)
    kartno = models.IntegerField(blank=True,null=True)
    kartay = models.IntegerField(blank=True,null=True)
    kartyil = models.IntegerField(blank=True,null=True)
    kartcvc = models.IntegerField(blank=True,null=True)
    email = models.CharField(blank=True,max_length=200 )
    
    def __str__(self):
        return self.adi


    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['adi','soyadi','adres','tel','sehir','ilce','posta','kartisim','kartno','kartay','kartyil','kartcvc']

class OrderProduct(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Prepared','Prepared'),
    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    urun = models.ForeignKey(Urun,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.urun.urun_adi
class Siparisler(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sepettekiurun = models.ForeignKey(Sepet,on_delete=models.CASCADE)
    kullanicibilgileri = models.ForeignKey(Order,on_delete=models.CASCADE,null = True)
    adet = models.IntegerField()
    fiyat = models.IntegerField()
    def __str__(self):
        return self.user.username
    
    
    
    
    




