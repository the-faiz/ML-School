from django.shortcuts import render
from django.views import View

# Create your views here.

class GradientDescentPrimer(View):
    def get(self,request,*args,**kwargs):
        return render(request,'gradient_descent_basics/gradient_descent_primer.html',{})

class GradientDescentCoding(View):
     def get(self,request,*args,**kwargs):
        return render(request,'gradient_descent_basics/coding_gradient_descent.html',{})

