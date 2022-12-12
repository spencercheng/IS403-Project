from django.http import HttpResponse
from django.shortcuts import render
from .models import *

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
     
def addCragPageView(request):
    if request.method == 'POST':
       crag = Crag()
       crag.cragName = request.POST['cragName']
       crag.city = request.POST['city']
       crag.state = request.POST['state']

       crag.save()

    return render(request, 'Climbing/addCrag.html')

def addWallPageView(request):
    data = Crag.objects.all()
    context= {
        "data": data
    }

    if request.method == 'POST':
       wall = Wall()
       wall.wallName = request.POST['wallName']
       wall.crag = request.POST['cragName']
       wall.save()

    return render(request, 'Climbing/addWall.html', context)

def addRoutePageView(request):
    data = Wall.objects.all()
    context= {
        "data": data
    }

    if request.method == 'POST':
       route = Route()
       route.routeName = request.POST['routeName']
       route.comments = request.POST['comments']
       route.description = request.POST['description']
       route.wall = request.POST['wallName']
       route.save()

    return render(request, 'Climbing/addRoute.html', context)