from django.shortcuts import render
from django.views import View

# Create your views here.
class LROneVariableHighLevel(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/LR_one_var_high_level.html',{})

class LROneVaribaleMathematics(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/mathematics.html',{})

class LROneVaribaleMathematics2(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/mathematics2.html',{})

class LROneVaribaleCoding(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/coding_of_LR_one_var.html',{})

class MultipleLinearRegression(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/multiple_linear_regression.html',{})

class OverfittingUnderfittingInLr(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/overfitting_underfitting_in_LR.html',{})

class LinearRegressionMetrics(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/linear_regression_metrics.html',{})

class LinearRegressionAssumptions(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/linear_regression_assumptions.html',{})

class LinearRegressionInterviewQuestions(View):
    def get(self, request, *args, **kwargs):
        return render(request,'LR_one_variable/linear_regression_interview_questions.html',{})
