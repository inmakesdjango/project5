from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method =='POST':
        username =request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        mailid = request.POST['email']
        password = request.POST['password']
        confirmpassword= request.POST['CONFIRM PASSWORD']
        if password==confirmpassword:
          if User.objects.filter(username=username).exists():
              messages.info(request ,"username already exist")
              return redirect ('register')
          elif User.objects.filter(email=mailid).exists():
              messages.info(request ,"mailid already exist")
              return redirect ('register')
          else:
              user =User.objects.create_user(username=username ,first_name=firstname ,last_name=lastname
                                                ,email=mailid ,password=password )
              user.save();
              return redirect('login')
              print("user created")
        else:

             messages.info(request,"password not matching")
             return redirect('register')
             return redirect()
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')