from django.shortcuts import render, redirect
from .models import Menu
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def recipe_list(request):
    objects = Menu.objects.all()
    return render(request, 'receipe_list.html', {'recipe_objects': objects})

def recipe_create(request):
    if request.method == 'POST':
        Menu.objects.create(
            recipe_name = request.POST['recipe_name'],
            ingredients = request.POST['ingredients'],
            process = request.POST['process'],
            image1 = request.FILES['image']
        )
        return HttpResponseRedirect(reverse('recipe_list'))
    
    return render(request, 'receipe_create.html')

def recipe_detail(request,id):
    object = Menu.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe_objects':object})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)  #compares the password and username

        if User is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/create/')

    return render(request, 'user_login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request. POST.get('last_name')
        username= request. POST.get ('username')
        password= request. POST.get ('password')

        user = User.objects.filter(username=username) 

        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request,'Account created Successfully')

        return redirect('/register/')
    
    return render(request, 'user_register.html')