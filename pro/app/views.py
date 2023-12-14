from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from . models import reg


# Create your views here.
def home(request):
    return render (request,'index.html')


def registr(request):
    if request.method=='POST':
        a=request.POST['s']
        b=request.POST['r']
        c=request.POST['u']
        d=request.POST['t']

        data=reg.objects.create(username=a,password=b,email=c,number=d)
        data.save()
    return render(request,'register.html')  
  
def login(request):
    if request.method=="POST":
        e=request.post['username']
        f=request.post['password']
        user=authenticate(username=e,password=f)
        if user is not None:
            login(request,user)
            return redirect('login')
        
    return render (request,'login.html') 
def success(request):
    return HttpResponse("User successfully logined")          