from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("read/<int:id>/", views.read, name="read"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
