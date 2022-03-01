import plotly.graph_objects as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from get_plots import get_scatter_plot


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
       html.Div([
           dcc.Graph(id='fig1'),
       ]) ,
       html.Div([
           html.H6('Time period (days)'),
           dcc.Slider(
               id='slider-day1',
               min=0,
               max=100,
               step=1,
               value=30,
               marks={i: str(i) for i in range(0, 100, 10)}
           ),
           html.H6('Number of breweries from the top'),
           dcc.Slider(
               id='slider-top1',
               min=0,
               max=500,
               step=50,
               value=500,
               marks={i: str(i) for i in range(0, 500, 50)})
       ])
])

@app.callback(
   dash.dependencies.Output('fig1', 'figure'),
   [dash.dependencies.Input('slider-day1', 'value'),
    dash.dependencies.Input('slider-top1', 'value')])
def output_fig(n_days, top_n):
    get_scatter_plot(n_days, top_n)
    
if __name__ == '__main__':
   app.run_server(debug=True)
