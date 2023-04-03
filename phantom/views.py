from .models import Cars_Dest
from django.shortcuts import render

# Create your views here.

# Create your views here.
def index(request):

 dests = Cars_Dest.objects.all()


 return render(request,'index.html',{'dests' : dests})