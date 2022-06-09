import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


########### Define your variables
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

for step in np.arange(0,101,0.5):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0,101,1),
            y = ((mu_arg(step)/(lambda_arg(step)+mu_arg(step)))+(lambda_arg(step)/(lambda_arg(step)+mu_arg(step)))*
                 1/np.exp(((lambda_arg(step)+mu_arg(step))*np.arange(0,101,1))))))

fig.data[10].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "λ Failure rate (failures per hour): " + str(0.1*i)}],
        label = str("%.2f" %(0.1*i))
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": " λ Failure rate (failures per hour): "},
    pad={"t": 50},
    steps = steps
)]

fig.update_layout(
    sliders=sliders,
    xaxis_title="Hours",
    yaxis_title="Availability",
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
    app.run_server()
