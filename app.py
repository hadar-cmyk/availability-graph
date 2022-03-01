import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

########### Define your variables

t = np.linspace(0, 10,1000)
mytitle='Availability Graph'
tabtitle='Graph'
myheading='Dependency between failure and recovery rates'
label1='hours'
githublink='https://github.com/dflymegold/availability-graph'


########### Set up the chart



function = go.Figure(date = (go.Scatter(t,np.sin(t))))



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=function
    ),
    html.A('Code on Github', href=githublink),
    
    ]
)

if __name__ == '__main__':
    app.run_server()
