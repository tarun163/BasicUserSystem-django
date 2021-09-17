from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginuser, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        users = UserInfo.objects.all()
        for user in users:
            print(user.username, user.email, user.address, user.created_on)
        context = {'success':True, 'users':users}    
        return render(request, 'home.html', context)
    else:
        return render(request, 'login.html')

def delete(request, id):
    UserInfo.objects.get(pk=id).delete()
    return redirect('home')

def edit(request, id):
    return redirect('home')    

def login(request):
    context = {'success':False}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserInfo.objects.get(email=email)
        print(user.email)
        if user is not None:
            pwd = user.password
            username = user.username
            user = authenticate(username=username, password=password)
            if user is not None:
                loginuser(request, user)
                # request.session['email'] = email
                return redirect('home')
            else:
                context = {
                    'success': True,
                    'msg': 'enter valid password'
                }
                return render(request, 'login.html', context)  
        else:
            context = {
                'success':True,
                'msg':'user not found'
            } 
        return render(request, 'login.html', context)             
    return render(request, 'login.html', context)

def signup(request):
    context = {'success':False}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('add')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        if password1 == password2 :
            user = UserInfo(username=username, password=password1, address=address, email=email)
            user.save()
            user = User.objects.create_user(username=username, email=email, password=password1) 
            user.save()          
            return redirect('login')
        else:
            context = {
                'success':True,
                'msg':'please enter both the password same'
            }
            return render(request, 'signup.html' ,context)      
    return render(request, 'signup.html' ,context)   

def log_out(request):
    logout(request)
    return redirect('login')         