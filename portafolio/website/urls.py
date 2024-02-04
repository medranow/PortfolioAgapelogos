from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("english", views.english, name="english"),
    path("czech", views.czech, name="czech")
]