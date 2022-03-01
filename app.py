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


function = go.Figure(data=[go.Scatter(x=t, y=np.sin(t))])


fig = go.Figure()

for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))))

    
fig.data[10].visible = True


steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
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
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='graph',
        figure=fig ),
        html.Div([
         html.H6(label1),
         dcc.Slider(
               id='slider-hours',
               min=0,
               max=20,
               step=1,
               value=1,
               marks={i: str(i) for i in range(0, 20, 1)}
             )]),
    html.Br(),
    html.A('Code on Github', href=githublink),
    ])

if __name__ == '__main__':
    app.run_server()
