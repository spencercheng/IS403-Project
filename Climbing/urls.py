from django.urls import path
from .views import indexPageView, aboutPageView, contactPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("about/", aboutPageView, name="about" ),
    path("contact/" , contactPageView, name="contact"),
]     