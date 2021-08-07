import os
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from . models import imagesUpload, Contactus
from MyImages import models

def register(request):
    
        if request.method == "POST":
                email = request.POST['email']
                username = request.POST['username']
                password = request.POST['password']
                repassword = request.POST['repassword']
                
                if User.objects.filter(email=email).exists():
                    print('email')
                    return redirect('register')

                elif User.objects.filter(username=username).exists():
                    print('name')
                    return redirect('register')

                elif password != repassword:
                    print('password')
                    return redirect('register')
                else:
                    user=User.objects.create_user(email=email,username=username,password=password)
                    user.save()

                    return redirect('login')

        else:
            return render(request, 'login/login.html')
   


def login(req):

    if req.method == "POST":
        # fm = Login(req.POST)
        username = req.POST['username']
        password = req.POST['password']

        user=auth.authenticate(username=username,password=password)
            
        if user is not None:
            if user.is_superuser:
                return redirect('login')
            else:
                auth.login(req,user)
                return redirect('dashboard')
                
        else:
            return redirect('login')
        
    else:
        return render(req, 'login/login.html')


def logout(req):
    auth.logout(req)    
    return redirect('login')


def dashboard(req):
    if req.user.is_authenticated:
        context= {'User':User}
        return render(req, 'index.html', context)
    else:
        return redirect('login')

def about(req):
    return render(req, 'about.html')

def gallery(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'gallery.html',{'natureImage':natureImage})

def contactus(req):
    contact = Contactus()
    if req.method == 'POST':
        contact.email = req.POST['email']
        contact.name = req.POST['name']
        contact.phone = req.POST['phone']
        contact.msg = req.POST['message']
        contact.save()
        return render(req, 'contactus.html')
        
    else:
        return render(req, 'contactus.html')

def nature(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/nature.html',{'natureImage':natureImage})

def food(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/food.html',{'natureImage':natureImage})

def health(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/health.html',{'natureImage':natureImage})

def travel(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/travel.html',{'natureImage':natureImage})

def animal(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/animal.html',{'natureImage':natureImage})

def fashion(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/fashion.html',{'natureImage':natureImage})

def athlete(req):
    natureImage = imagesUpload.objects.all()
    return render(req, 'category/athlete.html',{'natureImage':natureImage})
