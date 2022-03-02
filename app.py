import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

########### Define your variables

x=np.arange(0,5,0.1)
mytitle = 'Availability Graph'
tabtitle = 'Graph'
myheading = 'Dependency between failure and recovery rates'
label1 = 'hours'
githublink = 'https://github.com/dflymegold/availability-graph'

########### Set up the chart


fig = go.Figure()

def lambda_arg (step_):
    return ((1-10)/step_)
def mu_arg (step_):
    return (1/step_)

for step in range(1,100,1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=x,
            y = ((mu_arg(step)/(lambda_arg(step)+mu_arg(step)))+(lambda_arg(step)/(lambda_arg(step)+mu_arg(step)))*
                 np.exp(-((lambda_arg(step)+mu_arg(step))*x)))))

fig.data[10].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to hour: " + str(i+1)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=1,
    currentvalue={"prefix": "Hours: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='graph',
        figure=fig),
    html.Br(),
    html.A('Code on Github', href=githublink),
])

if __name__ == '__main__':
    app.run_server(debug=True)
