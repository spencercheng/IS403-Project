from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("routes/", routesPageView, name="routes" ),
    path("learnmore/" , learnMorePageView, name="learnmore"),
    path("about/", aboutPageView, name="about"),
    path("edit/", editPageView, name="edit"),
    path("addCrag/", addCragPageView, name="addCrag"),
    path("addWall/", addWallPageView, name="addWall"),
    path("addRoute/", addRoutePageView, name="addRoute"),
]     