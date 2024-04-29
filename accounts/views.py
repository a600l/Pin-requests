from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def loginview(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('new-request')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')