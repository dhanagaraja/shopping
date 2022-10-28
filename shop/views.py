from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def detail(request):
    return render(request, 'detail.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def LoginUser(request):
    
    if request.method=='POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        
        user = authenticate(username=username, password=    password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfuly Logged In!')
            redirect('shop')
        else:
            messages.error(request, "Wrong Credentials!")
            return redirect('home')
            
    return render(request, 'index.html', {'user':user})

def SignUp(request):

    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request,'Username already There!')
            return HttpResponseRedirect(request.path_info)
        
        if User.objects.filter(email=email):
            messages.error(request,'your email already There!')
            return HttpResponseRedirect(request.path_info)
        
        if not password == pass2 :
            messages.error(request, "Your Password Not Match")
            return HttpResponseRedirect(request.path_info)
        
        if not username.isalnum():
            messages.error(request, 'Wrong username only contain Letter and Numbers!')
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('index')
    
    return render(request, 'index.html')

def Logout(request):
    logout(request)
    messages.success(request,'Hey! You are Logout Successfully')
    return render(request, 'index.html')
