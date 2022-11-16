from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'Climbing/index.html')

def routesPageView(request):
    return render(request, 'Climbing/about.html')

def learnMorePageView(request):
    return HttpResponse("Learn More Page")

def aboutPageView(request):
    return HttpResponse("About Page")

def editPageView(request):
    return HttpResponse("Edit Page")

def addPageView(request):
    return HttpResponse("Add Page")