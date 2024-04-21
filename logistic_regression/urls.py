from django.urls import path
from . import views
from logistic_regression.views import  *

urlpatterns = [
    path('', LogisticRegressionOverview.as_view()),
    path('overview.html', LogisticRegressionOverview.as_view()),
    path('sigmoid.html', SigmoidFunction.as_view()),
    path('mathematics.html', LogisticRegressionMathematics.as_view()),
    path('MLE_details_in_logistic_regression.html', MLEInLogisticRegression.as_view()),

    
]