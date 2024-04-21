import pandas as pd 


class CreateDataForPlot():
    @classmethod
    def get_data_for_plot(self):
        income=[15,30,5,22,33,18,28,12,24,9,23,34,13,26,8,23,13,30,26,5,18,13,23,15,24,8,16,7,14,28,25,30]
        risk_score=[8,8,9,10,12,15,20,21,22,30,32,32,35,38,48,50,51,53,70,72,76,78,80,85,89,90,100,105,110,110,102,110]
        default_label=[0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1]
        color=[]
        for i in default_label:
            if i==1:
                color.append("yes")
            else:
                color.append("no")

        df=pd.DataFrame()
        df['income']=income
        df['risk_score']=risk_score
        df['default_label']=default_label
        df['default_class']=color
        df['size']=df['default_label']+ 1
        return df