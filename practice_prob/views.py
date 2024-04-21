from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def practice_prob(request):
    return render(request,'practice_prob/practice_prob.html',{})

def solve(request):
    return render(request,'practice_prob/mcq.html',{})
