from django.shortcuts import render,redirect
from .models import donors
# Create your views here.
def redirec(request):
    return render(request,'search.html')

def search(request):
    return render(request,'search.html')

def register(request):
    return render(request,'register.html')

def find(request):
    don=donors.objects.all()
    city = request.POST["city"]
    blood_group = request.POST["blood_group"]
    for d in don:
        if d.blood_group==blood_group and d.city==city :
            return render(request,'searched.html',{'name':d.name,'mob':d.mob_no} )
    else:
        return render(request,'searched.html')

def record(request):
    rec=donors()
    rec.name = request.POST["name"]
    rec.email = request.POST["email"]
    rec.mob_no = request.POST["mob_no"]
    rec.age = int(request.POST["age"])
    rec.blood_group = request.POST["blood_group"]
    rec.city = request.POST["city"]
    rec.gender = request.POST["gender"]
    rec.save()
    return redirect(register)

