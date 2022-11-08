from django.contrib import admin
from .models import *


# Register your models here.
class SepetAdmin(admin.ModelAdmin):
    list_display = ['user','urunler','adet','fiyat','is_deleted']
admin.site.register(Urun)
admin.site.register(Kategori)
admin.site.register(Subcategory)
admin.site.register(SeriNo)
admin.site.register(Sepet, SepetAdmin)
admin.site.register(KategoriFotograflari)
# class ShopCartAdmin(admin.ModelAdmin):
#     list_display = ['user','urun','adet','fiyat','tutar','urunler']
#     list_filter = ['user']
# admin.site.register(ShopCart,ShopCartAdmin)

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','urun','quantity','price','amount')
    can_delete = False
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display = ['adi','soyadi','tel','sehir',]
    list_filter = ['adi']
    readonly_fields = ('user','adres','sehir','tel','adi','soyadi','ilce')
    inlines = [OrderProductline]
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','urun','quantity','price','amount']
    list_filter = ['user']
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(Siparisler)

