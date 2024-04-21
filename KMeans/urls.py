from django.urls import path
from . import views
from KMeans.views import  *

urlpatterns = [
    path('', KMeansOverview.as_view()),
    path('overview.html', KMeansOverview.as_view()),
    path('mathematics.html', KMeansMathematics.as_view()),
    path('metrics_for_kmeans.html', KMeansMetrics.as_view()),
    path('kmeans_interview_questions.html', KMeansInterviewQuestions.as_view()),
    
]