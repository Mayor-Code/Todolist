from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('todoList:home-page')
        else:
            return redirect('todoList:login')


def logout(request):
    auth.logout(request)
    return redirect('todoList:login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username already exist')
            return redirect('todoList:register')
        if password2 != password:
            messages.info(request, "password doesn't match")
            return redirect('todoList:register')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email is already linked with another user')
            return redirect('todoList:register')
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return redirect('todoList:login')
    else:
        return render(request, 'register.html')
# Create your views here.
