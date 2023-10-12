from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from django.views import View
from .forms import Regform,loginform 

# Create your views here. 
class home(View):
    def get(self,request):
        return render(request,'home.html')

class reginput(View):            
    def get(self,request):
        con_dic={'Regform':Regform()}
        return render(request,'registration.html',context=con_dic)
    
class logininput(View):
    def get(self,request):
        con_dic={'loginform':loginform()}
        return render(request,'login.html',con_dic)
    
class Regviews(View):                      
    def post(self,request): 
        print(10)
        rf=Regform(request.POST)
        print(20)
        if rf.is_valid():
            print(30)
            rf=Reg(firstName=rf.cleaned_data["firstName"],
            lastname=rf.cleaned_data["lastname"],
            email=rf.cleaned_data["email"],
            username=rf.cleaned_data['username'],
            password=rf.cleaned_data["password"],
            confpassword=rf.cleaned_data["confpassword"])
            rf.save()
        return HttpResponse("registartion successfuly")

class loginview(View):
    def post(self,request):
        lf=loginform(request.POST)
        if lf.is_valid():
            res=Reg.objects.filter(username=lf.cleaned_data["username"],
                                   password=lf.cleaned_data["password"])
            if res:
                return HttpResponse("login sucess")
            else:
                return HttpResponse("loginfailed")
                                   
        
            
       

    