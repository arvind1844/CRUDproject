from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student

# Create your views here.

def addshowform(request):
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

    return render(request, "app1/addshow.html", {'form':fm})
