from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("routes/", routesPageView, name="routes" ),
    path("learnmore/" , learnMorePageView, name="learnmore"),
    path("about/", aboutPageView, name="about"),
    path("edit/", editPageView, name="edit"),
    path("add/", addPageView, name="add"),
    path("viewCrags/", viewCrags, name="viewCrags"),
    path("viewWalls/", viewWalls, name="viewWalls"),
    path("viewRoutes/", viewRoutes, name="viewRoutes"),
    path("editCrag/", editCrag, name="editCrag"),
    path("editWall/", editWall, name="editWall"),
    path("editRoute/", editRoute, name="editRoute"),
    path("delCrag/", delCrag, name="delCrag"),
    path("delWall/", delWall, name="delWall"),
    path("delRoute/", delRoute, name="delRoute"),
]     