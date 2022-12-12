from django.http import HttpResponse
from django.shortcuts import render, redirect
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
     
def addPageView(request):
    return render(request, 'Climbing/add.html')

def viewCrags(request):
    
    cragData = Crag.objects.all()

    context = {
        "cragData" : cragData
    }

    return render(request, "Climbing/ViewCrags.html", context)

def viewWalls(request):
    
    wallData = Wall.objects.all()

    context = {
        "wallData" : wallData
    }

    return render(request, "Climbing/viewWalls.html", context)

def viewRoutes(request):
    
    routeData = Route.objects.all()

    context = {
        "routeData" : routeData
    }

    return render(request, "Climbing/viewRoutes.html", context)

def editCrag(request):
    crag = Crag.objects.get(id = request.POST['cragID'])

    context = {
        'crag' : crag
    }

    return render(request, "Climbing/editCrag.html", context)

def editWall(request):
    wall = Wall.objects.get(id = request.POST['wallID'])

    context = {
        'wall' : wall
    }

    return render(request, "Climbing/editWall.html", context)

def editRoute(request):
    route = Route.objects.get(id = request.POST['routeID'])

    context = {
        'route' : route
    }

    return render(request, "Climbing/editRoute.html", context)


def delCrag(request):

    crag = Crag.objects.get(id = request.POST['cragID'])
    crag.delete()

    return redirect("viewCrags")


def delWall(request):

    wall = Wall.objects.get(id = request.POST['wallID'])
    wall.delete()

    return redirect("viewWalls")

def delRoute(request):

    route = Route.objects.get(id = request.POST['routeID'])
    route.delete()

    return redirect("viewRoutes")