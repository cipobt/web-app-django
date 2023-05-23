from django.urls import path, include
from . import views

urlpatterns = [
    path('portfolio', views.portfolio),
    path('blog', views.blog),
    path('', views.index),
]
