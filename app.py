import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output


app = dash.Dash()


slider = dcc.Slider(id='slider', value=1, min=0, max=20, step=1,
                    marks={key: str(key) for key in range(20)})


app.layout = html.Div([dcc.Graph(id='availability-graph'),
                       slider])


@app.callback(Output('availbility-graph', 'figure'),
              [Input('slider', 'value')])

def make_figure(slider):

    figure = {
        'data': [
             go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))))
        ],
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

    return figure



if __name__ == '__main__':
    app.run_server()
