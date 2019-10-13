from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.models import Users
from .forms import LoginForms
from .forms import UserForm

def crudops(request):
    dreamreal = Dreamreal(website = "www.polo.com", mail = "sorex@polo.com", 
    name = "sorex", phonenumber = "002376970")
    dreamreal.save()

def viewall(request):
   # userform = UserForm()
    users = Users.objects.all()
    return render(request, 'home.html',{ 'users': users})

def adduser(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    address = request.POST["address"]
    description = request.POST["description"]
    users = Users(name=name,phone=phone,email=email,address=address,description=description)
    users.save()

    print ("From Submited")
    #return render(request, 'home.html')
    return redirect('/viewall/')

def delete(request, id):
    instance = Users.objects.get(id=id)
    instance.delete()
    #return render(request, 'home.html')
    return redirect('/viewall/')


def edit(request,id):
   editusers = Users.objects.get(id=id)
   return render(request,'updated.html',{'editusers':editusers})
    #return redirect('/viewall/')

   
def addupdateduser(request):
    idd = request.POST["id"]
    name = request.POST["name"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    address = request.POST["address"]
    description = request.POST["description"]
    users = Users.objects.filter(id=idd).update(name=name,phone=phone,email=email,address=address,description=description)
    ##users = Users()
    #return render(request,'home.html')
    return redirect('/viewall/')
def login(request):
    if request.method=='POST':
        print(request.POST['username'])
        return HttpResponse("ok i am here dont worry") 
    else:
        form = LoginForms()
        return render(request,'login.html',{'form':form})


    





    

    
