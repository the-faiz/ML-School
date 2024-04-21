from django.urls import path
from . import views

urlpatterns = [
    path('/', views.practice_prob),
    path('/solve', views.solve, name='solve'),
]