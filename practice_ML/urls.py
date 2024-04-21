from django.urls import path
from practice_ML.views import  *

urlpatterns = [
    path('implement_linear_regression', LinearRegresionQ1.as_view()),
    path('code_linear_regression', LinearRegresion1.as_view()),
]

