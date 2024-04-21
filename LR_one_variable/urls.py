
from django.urls import path
from . import views
from LR_one_variable.views import  *

urlpatterns = [
    path('', LROneVariableHighLevel.as_view()),
    path('LR_one_var_high_level.html', LROneVariableHighLevel.as_view()),
    path('mathematics.html', LROneVaribaleMathematics.as_view()),
    path('mathematics2.html',LROneVaribaleMathematics2.as_view()),
    path('coding_of_LR_one_var.html',LROneVaribaleCoding.as_view()),
    path('multiple_linear_regression.html',MultipleLinearRegression.as_view()),
    path('linear_regression_metrics.html',LinearRegressionMetrics.as_view()),
    path('overfitting_underfitting_in_LR.html', OverfittingUnderfittingInLr.as_view()),
    path('linear_regression_assumptions.html', LinearRegressionAssumptions.as_view()),
    path('linear_regression_interview_questions.html', LinearRegressionInterviewQuestions.as_view()),
    
]