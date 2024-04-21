from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ml_base(request):
    return render(request,'base_template/base_ML_course.html',{})

def main(request):
    return render(request,'base_template/home_page.html',{})
