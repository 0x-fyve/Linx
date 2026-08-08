from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("favourite/<int:pk>/", views.favourite, name="favourite"),
]