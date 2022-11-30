from django.shortcuts import render, HttpResponse
from . models import User, Message
import time
from django.db.models import Q

def index(request):
    return render(request, 'chat/login.html', {"message": "Login to Continue!!!"})

def signup(request):
    return render(request, 'chat/signUp.html', {"message": "Create your Account!!!"})

def saveuser(request):
    name = request.GET['user']
    contact = request.GET['contact']
    password = request.GET['password']
    print(name, contact, password)
    if len(User.objects.filter(name = name)) != 0:
        return render(request, 'chat/signUp.html', {"message": "User already exists. Enter unique name!!!"})
    user = User.objects.create(name = name, contact = contact, password = password)
    user.save()
    return render(request, 'chat/login.html', {"message": "Account Created. Login to Continue!!!"})

def room(request):
    cur_user = request.GET["user"]
    friend = request.GET["friend"]
    if 'password' in request.GET:
        password = request.GET['password']
        if len(User.objects.filter(name = cur_user, password = password)) == 0:
            return render(request, 'chat/login.html', {"message": "Incorrect Credentials!!!"})
    all_user = User.objects.all()
    all_msg = Message.objects.filter(Q(sender = cur_user) | Q(receiver = cur_user))
    room_name = min(cur_user, friend) + max(cur_user, friend)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'cur_user': cur_user,
        'friend': friend,
        'all_user': all_user,
        'all_msg': all_msg
    })

def data(request):
    cur_user = request.GET["user"]
    friend = request.GET["friend"]
    msg = request.GET["msg"]
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    msg = Message.objects.create(sender = cur_user, receiver = friend, msg = msg, time = current_time)
    msg.save()
    return HttpResponse("Data Saved.")