from django.urls import path
from . import views
from Decision_Tree.views import  *

urlpatterns = [
    path('', DecisionTreeOverview.as_view()),
    path('overview.html', DecisionTreeOverview.as_view()),
    path('predictions_in_decision_tree.html', PredictionInDecisionTree.as_view()),
    path('basic_concepts_for_tree_model.html', BasicConceptsForTreeModel.as_view()),
    path('information_gain.html', InformationGainDecisionTree.as_view()),
    path('threshold_determination.html', ThresholdDeterminationDecisionTree.as_view()),
    path('decision_tree_algorithm.html', DecisionTreeAlgorithm.as_view()),
    path('hyperparameter_tuning.html', HyperParameterTuningDecisionTree.as_view()),
    path('tree_pruning.html', TreePruning.as_view()),
    
]