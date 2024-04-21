from django.shortcuts import render
from django.views import View


class LinearRegresionQ1(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request,'practice_ML/linear_regression_Q1.html',context)

class LinearRegresion1(View):
    def get(self, request, *args, **kwargs):

        code = """
def sum_of_list(x):
  return sum(x)

    
print("Code Output")
print(sum_of_list([1,2,3,4,5]))"""
        context = {'page_title': 'Code Linear Regression',
                   'question_title' : "Linear Regression",
                   'question_description' : 'Description1',
                   'input' : 'this is input1',
                   'output':'this is output', 
            'python_code': code}
        return render(request,'code_editor/code_editor.html',context)