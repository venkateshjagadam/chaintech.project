from django.shortcuts import render,redirect
from .models import *

# Create your views here.
#def IndexView(request):
   # return render(request,"app/index.html")

#def htmlform(request):
 #   return render(request,"app/Forms.html")

def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    name = request.POST['name']
    email = request.POST['email']

    newuser = Details.objects.create(Name=name,Email=email)
    return render(request,"app/show.html")

def ShowPage(request):
    all_data=Details.objects.all()
    return render(request,"app/show.html",{'key1':all_data})