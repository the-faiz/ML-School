from django.shortcuts import render
from django.views import View


class EnsembleModelOverview(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'ensemble_model/overview.html',context)


class EnsembleModelTypes(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'ensemble_model/ensemble_model_types.html',context)

class Stacking(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'ensemble_model/stacking.html',context)

class Bagging(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'ensemble_model/bagging.html',context)

class Boosting(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'ensemble_model/boosting.html',context)