from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
# from dash import Dash, html, dcc
import plotly.express as px
# from scipy.stats import norm
import pandas as pd
## import dash_app is required as dash_app contains plotly apps
from . import dash_app
from . import get_data

# Create your views here.
class DecisionTreeOverview(View):
    def get(self, request, *args, **kwargs):
        context={"overview_plot_Decision_tree":self.get_overview_plot(),
                  "split_one_plot_dt":self.get_split_one_plot(),
                  "split_two_plot_dt":self.get_split_two_plot()
                    }
        return render(request,'Decision_Tree/overview.html',context)
    
    def get_overview_plot(self):
        data= get_data.CreateDataForPlot.get_data_for_plot() #self.get_data_for_plot()
        fig=px.scatter(data,y='income',x='risk_score',color='default_class',
        color_discrete_sequence=["green", "orange"],size='size', title="fig 1 scatter plot of cutstomers")  
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def get_split_one_plot(self):
        data= get_data.CreateDataForPlot.get_data_for_plot() #self.get_data_for_plot()
        fig=px.scatter(data,y='income',x='risk_score',color='default_class',
        color_discrete_sequence=["green", "orange"],size='size', title="Split using Income variable")
        fig.add_hrect(y0=0,y1=14.4,fillcolor="red",opacity=0.3)
        fig.add_hrect(y0=14.6,y1=37,fillcolor="green",opacity=0.3)
        fig.add_hline(y=14.5,line_width=3, line_dash="dash", line_color="black")
        fig_div=plot(fig,output_type="div")
        return fig_div
    
    def get_split_two_plot(self):
        data=get_data.CreateDataForPlot.get_data_for_plot() # self.get_data_for_plot()
        fig=px.scatter(data,y='income',x='risk_score',color='default_class',
        color_discrete_sequence=["green", "orange"],size='size', title="Split using risk_score")
        fig.add_shape(type='rect',x0=0,y0=14.6,x1=95,y1=37,fillcolor="green",opacity=0.3)
        fig.add_hline(y=14.5,line_width=3, line_dash="dash", line_color="black")
        fig.add_trace(go.Scatter(
                        x=[95, 95],
                        y=[14.5, 36],
                        mode="lines",
                        line=go.scatter.Line(color="blue",dash="dash",width=3),
                        showlegend=False
                        ))
        fig.add_shape(type='rect', x0=95,y0=14.5,x1=120,y1=37,fillcolor='blue',opacity=0.3)
        fig.add_hrect(y0=0,y1=14.4,fillcolor="red",opacity=0.3)
        fig_div=plot(fig,output_type="div")
        return fig_div

                  
class BasicConceptsForTreeModel(View):
    def get(self, request, *args, **kwargs):
        context={"entropy_plot":self.createEntropyPlot(),
                    "gini_plot":self.createGiniPlot()
                }
        return render(request,'Decision_Tree/basic_concepts_for_tree_model.html',context)
    
    def createEntropyPlot(self):
        x= np.linspace(0,1,500)
        y=-(x*np.log(x)+(1-x)*np.log(1-x))
        df=pd.DataFrame()
        df['Probability for positive class']=x
        df['Entropy']=y 
        fig=px.line(df,x="Probability for positive class",y="Entropy",title="Entropy vs probability of positive class")
        fig.add_vrect(x0=0, x1=0.5,
              annotation_text="high probability for class = 0", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
        fig.add_vrect(x0=0.5, x1=1,
              annotation_text="high probability for class = 1", annotation_position="top right",
              fillcolor="red", opacity=0.25, line_width=0)
        
        fig.add_vline(x=0.5, line_dash="dash", fillcolor='black',line_width=3)
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def createGiniPlot(self):
        x= np.linspace(0,1,500)
        y=1- x*x-(1-x)*(1-x)
        df=pd.DataFrame()
        df['Probability for positive class']=x
        df['Gini']=y 
        fig=px.line(df,x="Probability for positive class",y="Gini",title="Gini vs probability of positive class")
        fig.add_vrect(x0=0, x1=0.5,
              annotation_text="high probability for class = 0", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
        fig.add_vrect(x0=0.5, x1=1,
              annotation_text="high probability for class = 1", annotation_position="top right",
              fillcolor="red", opacity=0.25, line_width=0)
        
        fig.add_vline(x=0.5, line_dash="dash", fillcolor='black',line_width=3)
        fig_div=plot(fig,output_type='div')
        return fig_div

class PredictionInDecisionTree(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'Decision_Tree/predictions_in_decision_tree.html',context)

class InformationGainDecisionTree(View):
    def get(self, request, *args, **kwargs):
        context=request.session.get("django_plotly_dash", dict())
        return render(request,'Decision_Tree/information_gain.html',context)

class ThresholdDeterminationDecisionTree(View):
    def get(self, request, *args, **kwargs):
        context=request.session.get("django_plotly_dash", dict())
        return render(request,'Decision_Tree/threshold_determination.html',context)

class DecisionTreeAlgorithm(View):
    def get(self, request, *args, **kwargs):
        context=request.session.get("django_plotly_dash", dict())
        return render(request,'Decision_Tree/decision_tree_algorithm.html',context)

class HyperParameterTuningDecisionTree(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'Decision_Tree/hyperparameter_tuning.html',context)

class TreePruning(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'Decision_Tree/tree_pruning.html',context)

