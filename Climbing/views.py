from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Universe!')  

def routesPageView(request):
    return HttpResponse("Routes page")

def learnMorePageView(request):
    return HttpResponse("Learn More Page")

def aboutPageView(request):
    return HttpResponse("About Page")

def editPageView(request):
    return HttpResponse("Edit Page")

def addPageView(request):
    return HttpResponse("Add Page")