from django.shortcuts import render,redirect
from  .models import User
from django.contrib.auth import authenticate
# Create your views here.

def reg(request):
    return render(request,"reg.html")

def insertData(request):

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password= request.POST.get('password')
        print(name,email,age)
        query=User(name=name,email=email,age=age,password=password)
        query.save()
    return render(request,"reg.html")

def login(request):
    data = User.objects.all()
    context = {"data": data}
    return render(request,"login.html",context)

def user_login(request):

    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.filter(name=name,password=password)
        if user :
            request.session['user']=name
            return render(request,"home.html")
        else:
            print("invalid creditnials")
            return render(request,"login.html")

def home(request):
    if 'name' in request.session:
        return render(request, "home.html")
    return redirect(user_login)

def user_logout(request):
    if 'user' in request.session:
        print('user')
        del request.session['user']
    return render(request,'login.html')

