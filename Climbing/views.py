from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# main page
def indexPageView(request) :
    return render(request, 'Climbing/index.html')

# adding views     
def addCragPageView(request):
    if request.method == 'POST':
       crag = Crag()
       crag.cragName = request.POST['cragName']
       crag.city = request.POST['city']
       crag.state = request.POST['state']

       crag.save()

    return render(request, 'Climbing/addCrag.html')

def submitEditCrag(request):
    if request.method == 'POST':
       crag = Crag.objects.get(id = request.POST['cragID'])
       crag.cragName = request.POST['cragName']
       crag.city = request.POST['city']
       crag.state = request.POST['state']

       crag.save()

    return redirect('viewCrags')

def addWallPageView(request):
    
    data = Crag.objects.all()
    context= {
        "data": data
    }
    return render(request, 'Climbing/addWall.html', context)

def submitWall(request):

    if request.method == 'POST':
        wall = Wall()
        wall.wallName = request.POST['wallName']
        cragID = request.POST['cragID']
        wall.crag = (Crag.objects.get(id = cragID))

        wall.save()

    return redirect("addWall")


def submitEditWall(request):

    if request.method == 'POST':
        wall = Wall.objects.get(id = request.POST['wallID'])
        wall.wallName = request.POST['wallName']
        cragID = request.POST['cragID']
        wall.crag = (Crag.objects.get(id = cragID))

        wall.save()

    return redirect("viewWalls")

def submitRoute(request):

    if request.method == 'POST':
       route = Route()
       route.routeName = request.POST['routeName']
       route.comments = request.POST['comments']
       route.description = request.POST['description']
       route.wall = (Wall.objects.get(id = request.POST['wall']))

       route.save()

    return redirect("addRoute")

def submitEditRoute(request):

    if request.method == 'POST':
       route = Route.objects.get(id = request.POST['routeID'])
       route.routeName = request.POST['routeName']
       route.comments = request.POST['comments']
       route.description = request.POST['description']
       route.wall = (Wall.objects.get(id = request.POST['wall']))

       route.save()

    return redirect("viewRoutes")

def addRoutePageView(request):
    data = Wall.objects.all()
    context= {
        "data": data
    }

    return render(request, 'Climbing/addRoute.html', context)

# viewing views
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

# edit views
def editCrag(request):
    crag = Crag.objects.get(id = request.POST['cragID'])

    context = {
        'crag' : crag
    }

    return render(request, "Climbing/editCrag.html", context)

def editWall(request):
    wall = Wall.objects.get(id = request.POST['wallID'])

    crags = Crag.objects.all()

    context = {
        'wall' : wall,
        'crags' : crags
    }

    return render(request, "Climbing/editWall.html", context)

def editRoute(request):
    route = Route.objects.get(id = request.POST['routeID'])

    walls = Wall.objects.all()
    
    context = {
        'route' : route,
        'walls' : walls
    }

    return render(request, "Climbing/editRoute.html", context)

# delete views
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
