
from django.urls import path
from moviesApp import views

urlpatterns = [
    path('movies', views.available_movies),
    path('add/<int:a>/<int:b>/', views.add)
]
