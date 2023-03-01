from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.main, name="Main"),
    path("about/", views.about, name="About"),
    path("book/", views.book, name="Book"),
    path("menu/", views.menu, name="Menu"),
    path("", views.main, name="Main"),
    path("menu_item/<int:pk>/", views.display_menu_item, name = "menu_item")
]