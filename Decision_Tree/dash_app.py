import dash
from dash import dcc, html

from django_plotly_dash import DjangoDash
from . import get_data
import plotly.express as px
import numpy as np

data = get_data.CreateDataForPlot.get_data_for_plot()

info_gain = DjangoDash('information_gain')   # replaces dash.Dash

info_gain.layout = html.Div([ 
        dcc.Graph(id="information-gain-plot"),
        html.H3(id='information-gain-output'),
        html.Hr(),
        html.H5("Try changing the threshold for income variable (Click on any value on the slider)"),
        dcc.Slider(

        data['income'].min(),
        data['income'].max(),
        value = 14.5,
        marks={i: str(i) for i in range(0, 35,5)},
        id='iformation-gain-slider'
        ),
        html.Hr()
])


@info_gain.callback(
    dash.dependencies.Output('information-gain-plot', 'figure'),
    dash.dependencies.Output('information-gain-output', 'children'),
    [dash.dependencies.Input('iformation-gain-slider', 'value')])
def update_fig(threshold):
    fig=px.scatter(data,y='income',x='risk_score',color='default_class',
    color_discrete_sequence=["green", "orange"],size='size', title="Split using Income variable")
    fig.add_hrect(y0=0,y1=threshold-0.1,fillcolor="red",opacity=0.2)
    fig.add_hrect(y0=threshold+0.1,y1=37,fillcolor="green",opacity=0.2)
    fig.add_hline(y=threshold,line_width=3, line_dash="dash", line_color="black")
    information_gain = compute_information_gain(data, 'default_class', 'income',threshold)
    output_str = "Threshold = {0}, Information gain = {1}".format(threshold, information_gain)
    # fig.update_layout(transition_duration=50)
    # fig_div=plot(fig,output_type="div")
    return fig, output_str


def compute_impurity(feature, impurity_criterion):
    """
    This function calculates impurity of a feature.
    Supported impurity criteria: 'entropy', 'gini'
    input: feature (this needs to be a Pandas series)
    output: feature impurity
    """
    probs = feature.value_counts(normalize=True)
    
    if impurity_criterion == 'entropy':
        impurity = -1 * np.sum(np.log(probs) * probs)
    elif impurity_criterion == 'gini':
        impurity = 1 - np.sum(np.square(probs))
    else:
        raise ValueError('Unknown impurity criterion')
        
    return(round(impurity, 3))

def compute_information_gain(df, target, feature_name, threshold, split_criterion='entropy'):
    """
    This function calculates information gain for splitting on 
    a particular descriptive feature for a given dataset
    and a given impurity criteria.
    Supported split criterion: 'entropy', 'gini'
    """  
    assert len(df)!=0, "data frame should be non empty"      
    entropy_before_split = compute_impurity(df[target], split_criterion)
    df_letf = df[df[feature_name]<threshold]
    w1 = len(df_letf)/len(df)
    df_right = df[df[feature_name]>=threshold]
    w2= len(df_right)/len(df)
    entropy_left = compute_impurity(df_letf[target], split_criterion)
    entropy_right = compute_impurity(df_right[target], split_criterion)
    entropy_after_split = w1*entropy_left + w2*entropy_right
    global data
    information_gain = (len(df)/len(data))*(entropy_before_split - entropy_after_split)
    return(round(information_gain,4))


decision_tree_iteration_1 = DjangoDash('decision_tree_iteration_1')
decision_tree_iteration_1.layout = html.Div([ 
    # html.H3('Decision tree step 1'),
    html.Hr(),
    html.H3("Select Variable for the data split"),
    dcc.RadioItems(['income','risk_score'], 'income',id='variable_selector', inline=True),
    html.H4('Select the split threshold of the choosen variable'),
    html.Div(id='slider'),
    html.Hr(),
    dcc.Graph(id='decision_tree_step_1'),
    html.H4(id='output_information_gain'),
    #html.H2("Output results of step 1"),
    #html.B(" Income variable gives best information gain at income = 14.5 & Information Gain = 0.1957"),
    #html.B(" risk_score variable gives best information gain at risk_score = 90 & Information Gain = 0.1828"),
    #html.Hr()

])

@decision_tree_iteration_1.callback(
    dash.dependencies.Output('slider', 'children'),
   [dash.dependencies.Input('variable_selector', 'value')])
def update_slider(variable_name):
    min_val=data[variable_name].min()
    max_val=data[variable_name].max()
    if variable_name=='income':
        value = 14.5
        steps=5
    else:
        value = 90
        steps = 10
    return dcc.Slider(min_val,max_val,value = value,
        marks={i: i for i in range(0, max_val ,steps)},id="slider_variable")


@decision_tree_iteration_1.callback(
dash.dependencies.Output('decision_tree_step_1', 'figure'),
dash.dependencies.Output('output_information_gain', 'children'),
[dash.dependencies.Input('slider_variable', 'value'),
dash.dependencies.Input('variable_selector', 'value')])
def update_fig(threshold, variable_name):
    #fig = make_subplots(rows=1, cols=2, column_widths=[0.5, 0.5])
    #trace1=go.Scatter(x=data['risk_score'].values,y=data['income'].values, mode='markers',
    #marker=dict(color=data['default_label'].values))
    #fig.add_trace(row=1,col=1, trace=trace1)
    # threshold = float(threshold)
    fig=px.scatter(data,y='income',x='risk_score',color='default_class',
    color_discrete_sequence=["green", "orange"],size='size', title=" Diagram 1: Data Split using {0} variable".format(variable_name))
    if variable_name=='income':
        fig.add_shape(type='rect',x0=-1,x1=120,y0=0,y1=threshold-0.1,fillcolor="red",opacity=0.3)
        fig.add_shape(type='rect',x0=-1,x1=120,y0=threshold+0.1,y1=37,fillcolor="green",opacity=0.3)
        fig.add_hline(y=threshold,line_width=3, line_dash="dash", line_color="black")
        information_gain = compute_information_gain(data, 'default_class', 'income',threshold)
    elif variable_name=="risk_score":
        fig.add_shape(type='rect',x0=-1,x1=threshold-0.1,y0=0,y1=37,fillcolor="red",opacity=0.3)
        fig.add_shape(type='rect',x0=threshold+0.1,x1=120,y0=0,y1=37,fillcolor="green",opacity=0.3)
        fig.add_vline(x=threshold,line_width=3, line_dash="dash", line_color="black")
        information_gain = compute_information_gain(data, 'default_class', 'risk_score',threshold)
    output_str = "Variable selected = {0}, Threshold = {1},  Information gain = {2}".format(variable_name, threshold, information_gain)
    return fig, output_str


# app for iteration 2 in decision tree

decision_tree_iteration_2 = DjangoDash('decision_tree_iteration_2')
decision_tree_iteration_2.layout = html.Div([
    html.Hr(),
    html.H3("Select Variable for the data split"),
    dcc.RadioItems(['income','risk_score'], 'risk_score',id='variable_selector', inline=True),
    html.H4('Select the split threshold of the choosen variable'),
    html.Div(id='slider_for_iteration_2'),
    html.Hr(),
    dcc.Graph(id='decision_tree_step_2'),
    html.H4(id='output_information_gain'),


])
@decision_tree_iteration_2.callback(
    dash.dependencies.Output('slider_for_iteration_2', 'children'),
   [dash.dependencies.Input('variable_selector', 'value')])
def update_slider_for_iteration_2(variable_name):
    min_val=data[variable_name].min()
    max_val=data[variable_name].max()
    if variable_name=='income':
        value = 22.2
        steps=5
        min_val = 15
    else:
        value = 95
        steps = 10
    return dcc.Slider(min_val,max_val,value = value,
        marks={i: i for i in range(0, max_val ,steps)},id="slider_variable")


@decision_tree_iteration_2.callback(
dash.dependencies.Output('decision_tree_step_2', 'figure'),
dash.dependencies.Output('output_information_gain', 'children'),
[dash.dependencies.Input('slider_variable', 'value'),
dash.dependencies.Input('variable_selector', 'value')])
def update_fig(threshold, variable_name):
    fig=px.scatter(data,y='income',x='risk_score',color='default_class',
    color_discrete_sequence=["green", "orange"],size='size', title="Diagram 2 : Data Split using {0} variable".format(variable_name))
    fig.add_hline(y=14.4,line_width=3, line_dash="dash", line_color="black")
    fig.add_shape(type='rect',x0=-1,x1=120,y0=0,y1=14.5,fillcolor="red",opacity=0.3)
    df = data[data['income']>=14.5]
    if variable_name=='income':
        fig.add_shape(type='rect',x0=-1,x1=120,y0=14.5,y1=threshold,fillcolor="blue",opacity=0.3)
        fig.add_shape(type='rect',x0=-1,x1=120,y0=threshold+0.1,y1=37,fillcolor="green",opacity=0.3)
        fig.add_hline(y=threshold,line_width=3, line_dash="dash", line_color="blue")
        information_gain = compute_information_gain(df, 'default_class', 'income',threshold)
    elif variable_name=="risk_score":
        fig.add_shape(type='rect',x0=-1,x1=threshold-0.1,y0=14.5,y1=37,fillcolor="green",opacity=0.3)
        fig.add_shape(type='rect',x0=threshold+0.1,x1=120,y0=14.5,y1=37,fillcolor="blue",opacity=0.3)
        fig.add_shape(type='line',x0=threshold,x1=threshold,y0=14.5,y1=37, line_width=3, line_dash="dash", line_color="blue")
        information_gain = compute_information_gain(data, 'default_class', 'risk_score',threshold)
    output_str = "Variable selected = {0}, Threshold = {1},  Information gain = {2}".format(variable_name, threshold, information_gain)
    return fig, output_str