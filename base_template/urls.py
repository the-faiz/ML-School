from django.urls import path
from . import views

urlpatterns = [
    path('ml_base/', views.ml_base),
    path('', views.main),
]