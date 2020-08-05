
from django.shortcuts import render,redirect
from .models import requests,messages
# Create your views here.

def request(request):
    return render(request,'request.html')


def requ(request):
    r=requests()
    r.name = request.POST["name"]
    r.hospital_name = request.POST["hospital"]
    r.mob_no = request.POST["mob_no"]
    r.city = request.POST["city"]
    r.blood_group = request.POST["blood_group"]
    r.save()
    return render(request,'request.html')

def contact(request):
    return render(request,'contact.html')

def message(request):
    m=messages()
    m.name = request.POST["name"]
    m.email = request.POST["email"]
    m.mes = request.POST["mes"]
    m.save()
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def terms(request):
    return render(request,'terms.html')