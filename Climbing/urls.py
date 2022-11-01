from django.urls import path
from .views import indexPageView, routesPageView, learnMorePageView, aboutPageView, editPageView, addPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("routes/", routesPageView, name="routes" ),
    path("learnmore/" , learnMorePageView, name="learnmore"),
    path("about/", aboutPageView, name="about"),
    path("edit/", editPageView, name="edit"),
    path("add/", addPageView, name="add"),
]     