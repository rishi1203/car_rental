from http.client import HTTPResponse
from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth
from .models import Cars_Dest



# Create your views here.

# Create your views here.
def index(request):

 dests = Cars_Dest.objects.all()
 return render(request,'index.html',{'dests' : dests})

def about(request): 
        return render(request,'about.html')
  
def fleet(request): 
        dests = Cars_Dest.objects.all()
        return render(request,'fleet.html',{'dests' : dests})                     
 
def blog(request): 
        return render(request,'blog.html')

def contact(request): 
        return render(request,'contact.html')    

def faq(request): 
        return render(request,'faq.html')  
def booknow(request): 
        return render(request,'booknow.html')              

def offers(request): 
        dests = Cars_Dest.objects.filter(offer=True)
        return render(request,'offers.html',{'dests' : dests})    


def team(request): 
        return render(request,'team.html')  

def terms(request): 
        return render(request,'terms.html')  

def testimonials(request): 
        return render(request,'testimonials.html')  

def blog_detail(request): 
        return render(request,'blog_detail.html')

       
        

              
 
