from django.shortcuts import render
from django.views import View
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np

# Create your views here.
class LogisticRegressionOverview(View):
    def get(self, request, *args, **kwargs):
        context={"overview_plot":self.get_overview_plot()}
        return render(request,'logistic_regression/overview.html',context)
    
    def get_overview_plot(self):
        x1=list(np.linspace(5,8.5,20))
        y1=[0 for i in range(len(x1))]
        x2=list(np.linspace(11.5,15,20))
        y2=[1 for i in range(len(x2))]
        x=x1+x2
        y=y1+y2
        trace1=go.Scatter(x=x, y=y, mode='markers',name='data points')
        # create data for sigmoid curve
        x_l= np.linspace(-7,7,num=1000)
        y_l=self.sigmoid(x_l)
        x_l=x_l+10
        trace2=go.Line(x=x_l,y=y_l,name='sigmoid')
        layout=dict(title='class vs credit utilization',xaxis=dict(title="credit utilization")
        ,yaxis=dict(title='y(class)'))
        fig=go.Figure(layout=layout).add_trace(trace1).add_trace(trace2)
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))

class SigmoidFunction(View):
    def get(self, request, *args, **kwargs):
        context={"sigmoid_plot":self.get_sigmoid_plot()}
        return render(request,'logistic_regression/sigmoid.html',context)
    
    def get_sigmoid_plot(self):
        x_l=np.linspace(-10,10,100)
        y_l=self.sigmoid(x_l)
        trace=go.Scatter(x=x_l,y=y_l,name='sigmoid function')
        layout=dict(title='Sigmoid Activation Function',xaxis=dict(title="x")
        ,yaxis=dict(title='sigmoid(x)'))
        fig=go.Figure(layout=layout).add_trace(trace)
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
    

class LogisticRegressionMathematics(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'logistic_regression/mathematics.html',context)


class MLEInLogisticRegression(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'logistic_regression/MLE_details_in_logistic_regression.html',context)
# Create your views here.
