from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginuser, logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        customer = request.user.username
        users = UserInfo.objects.all()
        context = {'success':True, 'users':users, 'customer':customer, 'msg':'Welcome ', 'class':'success'}    
        return render(request, 'home.html', context)
    else:
        return render(request, 'login.html')

def delete(request, id):
    UserInfo.objects.get(pk=id).delete()
    return redirect('home')

def edit(request, id):
    if request.method == 'POST':
        email = request.POST.get('email')
        address = request.POST.get('add')
        print(id, email, address)
        UserInfo.objects.filter(pk = id).update(email=email, address=address, created_on=datetime.datetime.now())
        User.objects.filter(pk = id).update(email=email)
        users = UserInfo.objects.all()
        context = {
                    'success': True,
                    'msg': 'your data is updated',
                    'class':'success',
                    'users':users
                }
        return render(request, 'home.html', context)
    return redirect('home')    

def login(request):
    context = {'success':False}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserInfo.objects.filter(email=email)
        if user is not None:
            pwd = user.password
            username = user.username
            user = authenticate(username=username, password=password)
            if user is not None:
                loginuser(request, user)
                return redirect('home')
            else:
                context = {
                    'success': True,
                    'msg': 'enter valid email or password',
                    'class':'danger'
                }
                return render(request, 'login.html', context)  
        else:
            context = {
                'success':True,
                'msg':'user not found',
                'class':'danger'
            } 
            return render(request, 'login.html', context)             
    return render(request, 'login.html', context)

def signup(request):
    context = {'success':False}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        que = UserInfo.objects.get(email = email)
        print(que)
        if que is None:
            address = request.POST.get('add')
            password1 = request.POST.get('password')
            password2 = request.POST.get('cpassword')
            if password1 == password2 :
                user = UserInfo(username=username, password=password1, address=address, email=email)
                user.save()
                user = User.objects.create_user(username=username, email=email, password=password1) 
                user.save()          
                context = {
                   'success':True,
                   'msg':'you are successfully registerd please login!',
                   'class':'success'
                }
                return render(request, 'login.html' ,context)
            else:
                context = {
                   'success':True,
                   'msg':'please enter both the password same',
                   'class':'danger'
                }
                return render(request, 'signup.html' ,context)      
        else:
            context = {
                   'success':True,
                   'msg':'email is already exist',
                   'class':'danger'
                }
            return render(request, 'signup.html' ,context)

    return render(request, 'signup.html' ,context)   

def log_out(request):
    logout(request)
    return redirect('login')         