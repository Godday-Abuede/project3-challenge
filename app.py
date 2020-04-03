import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly_express as px
import pandas as pd
from dash.dependencies import Input, Output, State

data = pd.read_csv("data.csv")

fig = px.scatter(
    data,
    x = "Date",
    y = "Open",
    color = "Open",
    template = "presentation"
)


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Amazon Stock Price Prediction"),
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
