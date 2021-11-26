from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.newpage, name="newpage"),
    path("wiki/<str:article>", views.entrypage, name="entrypage"),
    path("error", views.errorpage, name="errorpage"),
    path("search", views.search, name="search")
]
