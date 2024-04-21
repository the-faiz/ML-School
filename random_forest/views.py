from django.shortcuts import render
from django.views import View


class RandomForestOverview(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'random_forest/overview.html',context)


class RandomForestAlgorithm(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'random_forest/details_of_random_forest.html',context)

class RandomForestHyperparameterTuning(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'random_forest/hyperparameter_tuning.html',context)