import dash  # use Dash version 1.16.0 or higher for this app to work
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objs as go
from main import run_gen_algo
import pandas as pd
from dash import dash_table

results,x,y,z = run_gen_algo()

data = {'Results': results, 'X': x, 'Y': y, 'Z': z}
df = pd.DataFrame.from_dict(data)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout =  html.Div([
    dcc.Graph(
        figure=go.Figure(data=[go.Scatter(y=results)])
    ),
    dcc.Graph(
            figure=go.Figure(data=[go.Scatter(y=x)])
        ),
    dcc.Graph(
        figure=go.Figure(data=[go.Scatter(y=y)])
    ),
    dcc.Graph(
        figure=go.Figure(data=[go.Scatter(y=z)])
    ),
    dash_table.DataTable(
        id='Results',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)

# https://youtu.be/G8r2BB3GFVY
