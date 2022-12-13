from django.urls import path
from .views import *

urlpatterns = [
    # main page
    path("", indexPageView, name="index"), 
    # add
    path("addCrag/", addCragPageView, name="addCrag"),
    path("addWall/", addWallPageView, name="addWall"),
    path("addRoute/", addRoutePageView, name="addRoute"),
    path("submitWall/", submitWall, name="submitWall"),
    # edit
    path("submitRoute/", submitRoute, name="submitRoute"),
    path("submitEditWall/", submitEditWall, name="submitEditWall"),
    path("submitEditRoute/", submitEditRoute, name="submitEditRoute"),
    path("submitEditCrag/", submitEditCrag, name="submitEditCrag"),
    path("editCrag/", editCrag, name="editCrag"),
    path("editWall/", editWall, name="editWall"),
    path("editRoute/", editRoute, name="editRoute"),
    # view
    path("viewCrags/", viewCrags, name="viewCrags"),
    path("viewWalls/", viewWalls, name="viewWalls"),
    path("viewRoutes/", viewRoutes, name="viewRoutes"),
    # delete
    path("delCrag/", delCrag, name="delCrag"),
    path("delWall/", delWall, name="delWall"),
    path("delRoute/", delRoute, name="delRoute"),
]     