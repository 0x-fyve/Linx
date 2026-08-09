from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("favorite/<int:id>/", views.favorite, name="favorite"),
]