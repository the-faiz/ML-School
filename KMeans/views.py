from django.shortcuts import render
from django.views import View
import pandas as pd
from plotly.offline import plot
from sklearn.datasets import make_blobs
import plotly.express as px

# Create your views here.
class KMeansOverview(View):
    def get(self, request, *args, **kwargs):
        context={"kmeans_overview_plot":self.get_overview_plot()}
        return render(request,'KMeans/overview.html',context)
    
    def get_overview_plot(self):
        df=self.get_data()
        fig=px.scatter(df,x='Normalized income',y='Normalized spend',color='cluster',title='KMeans Clustering Output')
        fig_div=plot(fig,output_type='div')
        return fig_div
    
    def get_data(self):
        centers = [[1, 1], [-1, -1], [1, -1]]
        n_clusters = len(centers)
        X, labels_true = make_blobs(n_samples=500, centers=centers, cluster_std=0.5,random_state=10)
        df=pd.DataFrame(X,columns=['Normalized income','Normalized spend'])
        df['cluster']=labels_true
        return df


class KMeansMathematics(View):
    def get(self, request, *args, **kwargs):
        context={"elbow_curve":self.get_elbow_plot()}
        return render(request,'KMeans/mathematics.html',context)

    def get_elbow_plot(self):
        x=[1,2,3,4,5,6,7,8,9,10]
        y=[800,600,550,480,450,430,418,410,405,401]
        df=pd.DataFrame()
        df['K']=x
        df['wscc']=y
        fig=px.line(df,x='K',y='wscc',markers=True, title="Elbow Curve")
        fig_div=plot(fig,output_type='div')
        return fig_div

class KMeansMetrics(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'KMeans/metrics_for_kmeans.html',context)

class KMeansInterviewQuestions(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,'KMeans/kmeans_interview_questions.html',context)
