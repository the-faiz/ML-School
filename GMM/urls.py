from django.urls import path
from . import views
from GMM.views import  *

urlpatterns = [
    path('', GMMOverview.as_view()),
    path('overview.html', GMMOverview.as_view()),
    path('normal_distribution_overview.html', NormalDistribution.as_view()),
    path('mathematics.html', GMMMathematics.as_view()),
    path('hyperparameter_tuning.html', GMMHyperparameterTuning.as_view()),
    #path('kmeans_interview_questions.html', KMeansInterviewQuestions.as_view()),
    
]