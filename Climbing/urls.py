from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("routes/", routesPageView, name="routes" ),
    path("learnmore/" , learnMorePageView, name="learnmore"),
    path("addCrag/", addCragPageView, name="addCrag"),
    path("addWall/", addWallPageView, name="addWall"),
    path("submitWall/", submitWall, name="submitWall"),
    path("submitRoute/", submitRoute, name="submitRoute"),
    path("submitEditWall/", submitEditWall, name="submitEditWall"),
    path("submitEditRoute/", submitEditRoute, name="submitEditRoute"),
    path("submitEditCrag/", submitEditCrag, name="submitEditCrag"),
    path("addRoute/", addRoutePageView, name="addRoute"),
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