from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
import plotly.express as px
from scipy.stats import norm
from sklearn import mixture
import pandas as pd

# Create your views here.
class GMMOverview(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'GMM/overview.html',context)


class NormalDistribution(View):
    def get(self, request, *args, **kwargs):
        context={"mean_effect_1d": self.get_1d_mean_plot(),
                "std_effect_1d":self.get_1d_std_plot(),
                "2d_normal_dist":self.get_2d_plot()
                }
        return render(request,'GMM/normal_distribution_overview.html',context) 

    def get_1d_mean_plot(self):
        x1,y1=self.get_1d_data(25,10)
        x2,y2=self.get_1d_data(35,10)
        x3,y3=self.get_1d_data(45,10)
        trace1=go.Line(x=x1,y=y1,name='mean = 25 , std = 10')
        trace2=go.Line(x=x2,y=y2,name='mean = 35 , std = 10')
        trace3=go.Line(x=x3,y=y3,name='mean = 45 , std = 10')
        layout=dict(title='Effect of mean on normal distribution',xaxis=dict(title="x")
        ,yaxis=dict(title='pdf'))
        fig=go.Figure(layout=layout).add_trace(trace1).add_trace(trace2).add_trace(trace3)
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def get_1d_std_plot(self):
        x1,y1=self.get_1d_data(45,5)
        x2,y2=self.get_1d_data(45,10)
        x3,y3=self.get_1d_data(45,15)
        trace1=go.Line(x=x1,y=y1,name='mean = 45 , std = 5')
        trace2=go.Line(x=x2,y=y2,name='mean = 45 , std = 10')
        trace3=go.Line(x=x3,y=y3,name='mean = 45 , std = 15')
        layout=dict(title='Effect of standard deviation on normal distribution',xaxis=dict(title="x")
        ,yaxis=dict(title='pdf'))
        fig=go.Figure(layout=layout).add_trace(trace1).add_trace(trace2).add_trace(trace3)
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def get_1d_data(self,mu,sigma):
        x = np.linspace(-10,90,1000)
        y=norm.pdf(x,loc=mu,scale=sigma)
        return x,y
    
    def get_2d_plot(self):
        df=self.get_2d_data()
        fig = px.scatter(df, x='x', y='y', color='cov',
                facet_col='cov', facet_col_wrap=2)
        fig.update_xaxes(matches=None) # for independent x axis
        fig.update_yaxes(matches=None) # for independent y axis
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def get_2d_data(self):
        mean = [0, 0]
        df1=pd.DataFrame()
        cov_00 = [[10, 0], [0, 10]]  # diagonal covariance
        x1, y1 = np.random.multivariate_normal(mean, cov_00, 5000).T
        df1['x']=x1
        df1['y']=y1
        df1['cov']="[[10, 0],[0, 10]]"
        cov_01 =[[10, 0], [0, 100]] 
        x2, y2 = np.random.multivariate_normal(mean, cov_01, 5000).T
        df2=pd.DataFrame()
        df2['x']=x2
        df2['y']=y2
        df2['cov']="[[10, 0],[0, 100]]"
        cov_10 = [[10, -6], [-6, 10]]
        x3, y3 = np.random.multivariate_normal(mean, cov_10, 5000).T
        df3=pd.DataFrame()
        df3['x']=x3
        df3['y']=y3
        df3['cov']= "[[10, -6],[-6, 10]]"
        cov_11 = [[10, 8], [8, 10]]
        x4, y4 = np.random.multivariate_normal(mean, cov_11, 5000).T
        df4=pd.DataFrame()
        df4['x']=x4
        df4['y']=y4
        df4['cov']= "[[10, 8],[8, 10]]"
        ## df2 is not added because visual effects are not clear
        df=pd.concat([df1,df3,df4], ignore_index=True)
        return df




class GMMMathematics(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'GMM/mathematics.html',context)  

class GMMHyperparameterTuning(View):
    def get(self, request, *args, **kwargs):
        context={"hyperparameter":self.get_plot_for_hyperparameters()}
        return render(request,'GMM/hyperparameter_tuning.html',context)  
    
    def get_plot_for_hyperparameters(self):
        df = self.get_data_for_plot(10)
        fig = px.line(df, x="number of cluster", y="BIC",
             color='Covariance type', title="hyperparameter tuning")
        fig_div=plot(fig,output_type='div')
        return fig_div 
    
    def get_data_for_plot(self,num_cluster):
        # Number of samples per component
        n_samples = 500

        # Generate random sample, two components
        np.random.seed(0)
        C = np.array([[0.0, -0.1], [1.7, 0.4]])
        X = np.r_[
            np.dot(np.random.randn(n_samples, 2), C),
            0.7 * np.random.randn(n_samples, 2) + np.array([-6, 3]),
        ]

        lowest_bic = np.infty
        bic = []
        n_components_range = range(1, num_cluster)
        cv_types = ["spherical", "tied", "diag", "full"]
        cv_list=[]
        clus_list=[]
        for cv_type in cv_types:
            for n_components in n_components_range:
                # Fit a Gaussian mixture with EM
                gmm = mixture.GaussianMixture(
                    n_components=n_components, covariance_type=cv_type
                )
                gmm.fit(X)
                bic.append(gmm.bic(X))
                cv_list.append(cv_type)
                clus_list.append(n_components)
                if bic[-1] < lowest_bic:
                    lowest_bic = bic[-1]
                    best_gmm = gmm


        df =pd.DataFrame()
        df['BIC']=bic
        df['number of cluster']=clus_list
        df['Covariance type']=cv_list
        return df
 

# Create your views here.
