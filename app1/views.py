from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import *
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_name = request.POST.get('room_name')
        room_obj, _ = Room.objects.get_or_create(room_name=room_name)

        print(room_obj)

        return redirect(f'/chat/{room_name}/?name={name}')
    return render(request , 'app1/home.html')


def chat(request , room_name):
    print(room_name)
    room_obj = Room.objects.filter(room_name=room_name).first()
    total_messages_of_room = room_obj.room.all()
    # name=name
    # print(name)
    context = {'room_name' : room_name,"total_messages":total_messages_of_room}
    return render (request , 'app1/chat.html' , context)


def register(request):
    if request.method=="POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        password = request.POST.get("password")
        try:
           user_exists=User.objects.get(username=username)
           messages.error(request, 'username already exist')
              # return HttpResponse("Username already taken")


        except User.DoesNotExist:




            user = User(username=username,first_name=name)

            print(user)
            user.set_password(password)
            print(user)
            user.save()
            messages.success(request, 'hello {} your registration has been done succesfully'.format(name))
    return render(request,"app1/register.html")

def loginView(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("home")
    return render(request,"app1/login.html")




