from django.shortcuts import render

# Create your views here.

def addshowform(request):
    return render(request, "app1/addshow.html")
