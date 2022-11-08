from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2'] 
        
        if sifre1 == sifre2:
            if User.objects.filter(username=kullanici).exists():
                messages.error(request,'Kullanıcı adı alınmış')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email alınmış')
                return redirect('register')
            elif len(sifre1) < 6:
                messages.error(request,'Şifre 6 karakterden az olamaz')
                return redirect('register')
            elif kullanici in sifre1:
                messages.error(request,'Şifre kullanıcı adı benzer olamaz')
                return redirect('register')
            else:
                user = User.objects.create_user(username=kullanici,email=email,password=sifre1)
                user.save()
                messages.success(request,'Başarıyla kayıt oldunuz')
                return redirect('login')
        else:
            messages.error(request,'Şifreler uyuşmuyor')
            return redirect('register')
    return render(request,'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']
        user = authenticate(request,username=kullanici,password=sifre)
        if user is not None:
            login(request,user)
            messages.success(request,'Başarıyla giriş yaptınız')
            return redirect('index')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request,'login.html')    
def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla çıkış yaptınız')
    return redirect('index')

def order_details(request):
    
    return render(request,'order_details.html')
@login_required(login_url='login')
def profil(request):
    user = request.user
    if request.method == 'POST':
        kullaniciguncelle = request.POST['kullaniciguncelle']
        emailguncelle = request.POST['emailguncelle']
        if User.objects.filter(username=kullaniciguncelle).exists():
            messages.error(request,'Kullanıcı adı alınmış')
            return redirect('profil')
        elif User.objects.filter(email=emailguncelle).exists():
            messages.error(request,'Email alınmış')
            return redirect('profil')
        
        else:
            user.username = kullaniciguncelle
            user.email = emailguncelle
            user.save()
            messages.success(request,'Başarıyla güncellendi')
            print("kasım")
            return redirect('index')
        
    context = {
        'user':user
        
    }
    
    
    return render(request,'profil.html',context)


def sifredegistir(request):
    user = request.user
    eskisifre = ''
    if request.method == 'POST':
        eskisifre = request.POST['eskisifre']
        newsifre = request.POST['newsifre']
        newsifre2 = request.POST['newsifre2']
        
        if newsifre == newsifre2:
            degis = authenticate(request, username = user, password = eskisifre)
            if degis is not None:
                user.set_password(newsifre)
                user.save()
                messages.success(request,'Şifre başarıyla değiştirildi')
                return redirect('index')
            else:
                messages.error(request, 'Eski şifre hatalı')
                return redirect('sifredegistir')
        # if eskisifre == user.check_password:
        #     if eskisifre == newsifre:
        #         messages.error(request,'Eski şifre ile yeni şifre aynı olamaz')
        #         return redirect('sifredegistir')
        #     else:
            
        #         if newsifre == newsifre2:
        #             if len(newsifre) < 6:
        #                 messages.error(request,'Şifre 6 karakterden az olamaz')
        #                 return redirect('sifredegistir')
        #             if user.username in newsifre:
        #                 messages.error(request,'Şifre kullanıcı adı benzer olamaz')
        #                 return redirect('sifredegistir')
        #             else:
        #                 user.check_password = (newsifre)
        #                 user.save()
        #                 messages.success(request,'Başarıyla güncellendi')
        #                 return redirect('index')
        #         else:
        #             messages.error(request,'Şifreler uyuşmuyor')
        #             return redirect('sifredegistir')
        # else:
        #     messages.error(request,'Eski şifre hatalı')
        #     return redirect('sifredegistir')
                
    context = {
        'user':user,
        'eskisifre':eskisifre
        
    }    
    
    
    return render(request,'sifredegistir.html',context)

