from django.urls import path
from . import views
from ensemble_model.views import  *

urlpatterns = [
    path('', EnsembleModelOverview.as_view()),
    path('overview.html', EnsembleModelOverview.as_view()),
    path('ensemble_model_types.html', EnsembleModelTypes.as_view()),
    path('stacking.html', Stacking.as_view()),
    path('bagging.html', Bagging.as_view()),
    path('boosting.html', Boosting.as_view())
    
]