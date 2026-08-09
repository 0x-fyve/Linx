from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("favorite/<int:id>/", views.favorite, name="favorite"),
    path("delete/<int:id>/", views.delete_translation, name="delete_translation"),
]