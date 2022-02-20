from dash import Dash, dcc, html, Input, Output
import altair as alt
from vega_datasets import data

cars = data.cars()

app = Dash(__name__, external_stylesheets=[
           'https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    dcc.Input(id='widget-1'),
    html.Div(id='widget-2'),
    html.Div('Hello blue dash', style={'color': 'blue', 'fontSize': 44}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('Hi there', id='my-para', style={'background-color': 'red'}),
    'This is my slider',
    dcc.Slider(min=0, max=5, value=2, marks={0: '0', 5: '5'}),
    'This is my dropdown',
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'}],
        placeholder='Select a city here...'),
    'This is my dropdown selection',
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'}],
        value='SF', multi=True),
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='Horsepower',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns])
], style={'marginTop': 50})


@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(cars).mark_point().encode(
        x=xcol,
        y='Displacement',
        tooltip='Horsepower').interactive()
    return chart.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)
