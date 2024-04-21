from django.urls import path
from . import views
from random_forest.views import  *

urlpatterns = [
    path('', RandomForestOverview.as_view()),
    path('overview.html', RandomForestOverview.as_view()),
    path('details_of_random_forest.html', RandomForestAlgorithm.as_view()),
    path('hyperparameter_tuning.html', RandomForestHyperparameterTuning.as_view()),
    
    
]