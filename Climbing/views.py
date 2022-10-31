from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Universe!')  

def aboutPageView(request):
    return HttpResponse("About page")

def contactPageView(request):
    return HttpResponse("Contact Page")