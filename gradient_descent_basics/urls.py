from django.urls import path
from . import views
from gradient_descent_basics.views import  *

urlpatterns = [
    path('', GradientDescentPrimer.as_view()),
    path('gradient_descent_primer.html', GradientDescentPrimer.as_view()),
    path('coding_gradient_descent.html', GradientDescentCoding.as_view()),
]