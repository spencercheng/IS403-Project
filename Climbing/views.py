from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'Climbing/index.html')

def routesPageView(request):
    return render(request, 'Climbing/routes.html')

def learnMorePageView(request):
    return render(request, 'Climbing/learnmore.html')

def aboutPageView(request):
    return render(request, 'Climbing/about.html')

def editPageView(request):
     return render(request, 'Climbing/edit.html')
     
def addPageView(request):
    return render(request, 'Climbing/add.html')