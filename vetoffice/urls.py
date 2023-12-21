from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fortune/", views.fortune, name="fortune"),
    path("detail/<petname>", views.detail, name="detail"),
]
