from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    kategori = ''
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        
        kategori = KategoriFotograflari.objects.filter(kategori__isim = search)
        urunler = Urun.objects.filter(
            Q(urun_adi__icontains=search) |
            Q(kategori__isim__icontains=search) 
        )
        
    context = {
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler,
        'kategori':kategori,
    }
    return render(request,'index.html',context)
def detay(request,id):
    urunum = Urun.objects.get(id = id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            print('içerik test')
            urun = request.POST['sepet'] 
            adett = request.POST['adet']
            if Sepet.objects.filter(user = request.user, urunler = urunum).exists():
                sepet = Sepet.objects.get(user = request.user, urunler = urunum)
                sepet.adet += int(adett)
                sepet.fiyat += int(adett) * int(urunum.urun_fiyat)
                sepet.save()
            else:
                sepet = Sepet.objects.create(user = request.user , urunler = urunum, adet = adett,  fiyat = int(adett) * int(urunum.urun_fiyat))
                sepet.save()
            ''' if Sepet.objects.filter(user = request.user).exists(): #eğer böyle bir kullanıcı varsa
                sepet = Sepet.objects.get(user = request.user) 
                if Sepet.objects.filter(urunler = urun, user = request.user).exists():
                    messages.error(request, 'Bu içerik zaten Sepetinize eklenmiş.')
                    return redirect('index') #yönlendirme
                sepet.urunler.add(urun) # en sonda eğer eklenmemişse sepete ekler
                sepet.adet += int(adett)
                sepet.save()
                messages.success(request, 'İçerik Sepete  eklendi.')
                return redirect('index')
            else:
                sepet = Sepet.objects.create(user = request.user) #eğer sepet hiç oluşmamışsa sepet nesnesi üretilir
                sepet.urunler.add(urun) #direk olarak sepete ekler
                sepet.save()#sepeti kaydeder
                messages.success(request, 'İçerik Sepetinize eklendi.')
                return redirect('index') '''
    else:
        if request.method == 'POST':
            messages.error(request, 'İçeriği sepetinize eklemek için lütfen giriş yapınız veya kaydolunuz.')
            return redirect('login')
    
    context = {
        'urun':urunum,
    }
    return render(request,'üründetay.html',context)
@login_required(login_url='login')    
def sepet(request):
    urunler = Sepet.objects.filter(user = request.user)
    toplam = 0
    for i in urunler:
        toplam += i.fiyat
    if 'trash' in request.POST:
        sil = request.POST['sil']
        silinen = Sepet.objects.filter(user = request.user).get(id = sil).delete()
        print("sil",sil)
        # silinen.delete()
        silinen.save()
        print(silinen)
        return redirect('sepet')
    if 'eksi' in request.POST:
        print('ds')
        sil = request.POST['sil']
        silinen = Sepet.objects.filter(user = request.user).get(id = sil)
        silinen.adet -= 1
        silinen.fiyat -= int(silinen.urunler.urun_fiyat)
        silinen.save()
        return redirect('sepet')
    if 'arti' in request.POST:
        print('ds')
        sil = request.POST['sil']
        silinen = Sepet.objects.filter(user = request.user).get(id = sil)
        silinen.adet += 1
        silinen.fiyat += int(silinen.urunler.urun_fiyat)
        silinen.save()
        return redirect('sepet')

    context = {
        # 'listem':listem,
        'urunler':urunler,
        'toplam':toplam,
    }
    return render(request,'sepet.html',context)
@login_required(login_url='login')
def checkout(request):
    user = request.user
    # form = OrderForm()
    siparis = Siparisler.objects.filter(user = user)
    urunler = Sepet.objects.filter(user = request.user)
    toplam = 0
    for i in urunler:
        toplam += i.fiyat
    
    if request.method == 'POST':
        userid = request.POST['userid']
        adi = request.POST['adi']
        soyadi = request.POST['soyadi']
        sehir = request.POST['sehir']
        ilce = request.POST['ilce']
        adres = request.POST['adres']
        tel = request.POST['tel']
        posta = request.POST['posta']
        kartisim = request.POST['kartisim']
        kartno = request.POST['kartno']
        kartay = request.POST['kartay']
        kartyil = request.POST['kartyil']
        kartcvc = request.POST['kartcvc']
        email = request.POST['email']
        
        if user.is_authenticated:
            if urunler is not None:
                siparisim = Order.objects.create(user = user, adi = adi, soyadi = soyadi, sehir = sehir, ilce = ilce, adres = adres, tel = tel, posta = posta, kartisim = kartisim, kartno = kartno, kartay = kartay, kartyil = kartyil, kartcvc = kartcvc,email = email)
                siparisim.save()
                messages.success(request, 'Siparişiniz alınmıştır. Teşekkür ederiz.')
                return redirect('index')    
                
                        
                        
            else:
                messages.error(request, 'Sepetinizde ürün bulunmamaktadır.')
                return redirect('index')
        else:
            messages.error(request, 'Lütfen giriş yapınız.')
            return redirect('login')
    context = {
        'siparis':siparis,
        'urunler':urunler,
        'user':user,
        'toplam':toplam,
        # 'form':form,
    }
        
    return render(request,'checkout.html',context)


def siparisler(request):
    user = request.user
    if user.is_authenticated:
        sepet = Sepet.objects.filter(user = user)
        bilgi = Order.objects.filter(user = user)
        print(sepet)
        if bilgi is not None:
            for i in bilgi:
                print(i)
        else:
            messages.error(request, 'Siparişiniz bulunmamaktadır.')
            return redirect('index')
    else:
        messages.error(request, 'Lütfen giriş yapınız.')
        return redirect('login')
    context = {
        'bilgi':bilgi,
        'sepet':sepet,
        'user':user,
    }
    
    print(i)
    return render(request,'order-index.html',context)
def adres (request):
    return render(request,'adres.html')











































































# kategori = Kategori.objects.all()
    # sepet = Sepet.objects.filter(user = user)
    # urun = Urun.objects.get(id = id)
    # total = 0
    # for rs in sepet:
    #     total += rs.urun.urun_fiyat * rs.adet
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         data = Order()
    #         data.first_name = form.cleaned_data['first_name']
    #         data.last_name = form.cleaned_data['last_name']
    #         data.phone = form.cleaned_data['phone']
    #         data.address = form.cleaned_data['address']
    #         data.city = form.cleaned_data['city']
    #         data.country = form.cleaned_data['country']
    #         data.user_id = user.id
    #         data.total = total
    #         data.ip = request.META.get('REMOTE_ADDR')
    #         ordercode = 123456789
    #         data.code = ordercode
    #         data.save()
    #         #move sepet to orderproduct
    #         sepet = Sepet.objects.filter(user = user)
    #         for rs in sepet:
    #             detail = OrderProduct()
    #             detail.order_id = data.id
    #             detail.user_id = user.id
    #             detail.product_id = rs.urun.id
    #             detail.quantity = rs.adet
                
    #             urun = Urun.objects.get(id = rs.urun.id)
    #             urun.urun_adet -= rs.adet
    #             urun.save()
                
    #             detail.price = rs.urun.urun_fiyat
    #             detail.amount = rs.urun.urun_fiyat * rs.adet
    #             detail.save()
    #         messages.success(request, 'Siparişiniz başarıyla alınmıştır. Teşekkür ederiz.')
    #         return redirect('index')
    #     else:
    #         messages.error(request, 'Siparişiniz alınırken bir hata oluştu.')
    #         return redirect('checkout')
    
    # form = OrderForm()
    # profile = User.objects.get(user_id = user.id)
    # context = {
    #     'sepet':sepet,
    #     'total':total,
    #     'form':form,
    #     'profile':profile,
    #     'kategori':kategori,
    # }
    # return render(request,'checkout.html',context)