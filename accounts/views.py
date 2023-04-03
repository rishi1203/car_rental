from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
 

def login(request):
        if request.method != 'POST':
                return render(request,'login.html')
        username = request.POST['username']
        psw = request.POST['psw']
        User =auth.authenticate(username=username,password=psw)
        if User is not None:
                auth.login(request,User)
                return redirect("/")
        else:
                messages.info(request,'invalid credentials')
                return redirect('login')       

def register(request):
        if request.method != 'POST':
                return render(request,'register.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        
        if psw == psw_repeat:
          if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
          elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('register')
          else:
            user = User.objects.create_user(username=username, password=psw,first_name=first_name,last_name=last_name,email=email)
            user.save()
            print('User Created')
           
            user =auth.authenticate(username=username,password=psw)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,'invalid credentials')
                return redirect('login')  
            

        else:
          messages.info(request,'Password not matching....')  
          return redirect('register') 

def logout(request):
        auth.logout(request)    
        return redirect('/')           
def booknow(request):
  if request.method != 'POST':
    return render(request,'register.html')
  pick_up = request.POST['pick_up']
  return_location = request.POST['return_location']
  pick_up_date = request.POST['pick_up_date']
  return_date = request.POST['return_date']
  name = request.POST['name']
  email = request.POST['email']
  mob_no = request.POST['mob_no']