from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
from django.http import HttpResponseRedirect

# Create your views here.

def addshowform(request):
    data = Student.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            std = Student(name=nm,email=em,password=pwd)
            std.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    return render(request, "app1/addshow.html", {'form':fm,'data':data})

def deletedata(request,id):
    pi = Student.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect("/")

def updatedata(request, id):
    message = "Updated Successfully"
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            return render(request, "app1/updatedata.html", {'form':fm,'msg':message})
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, "app1/updatedata.html", {'form':fm})

         

