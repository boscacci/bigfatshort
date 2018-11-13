import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from pkg import app
from pkg.models import *
import pdb

# edu_levels = ['03','04','06','08','09']
expense_cats = ['income', 'housing', 'foodhome','foodaway','health','alcbevg','apparel','trans','entrtain']

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='expense_1',
                options=[{'label': i, 'value': i} for i in expense_cats],
                value='Year'
            ),
        ],style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='expense_2',
                options=[{'label': i, 'value': i} for i in expense_cats],
                value='USD'
            ),

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    # dcc.Slider(
    #     id='year--slider',
    #     min=df['Year'].min(),
    #     max=df['Year'].max(),
    #     value=df['Year'].max(),
    #     marks={str(year): str(year) for year in df['Year'].unique()}
    # )
])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('expense_1', 'value'),
     dash.dependencies.Input('expense_2', 'value')])
     # dash.dependencies.Input('xaxis-type', 'value'),
     # dash.dependencies.Input('yaxis-type', 'value')])
     # dash.dependencies.Input('year--slider', 'value')])
def update_graph(expense_1, expense_2):
    # dff = df[df['Year'] == year_value]
    years = list(range(2002,2013))
    return {
        'data': [go.Scatter(
            x = years,
            y = [getattr(item, expense_1) for item in By_Edu.query.filter(By_Edu.edu_level == '03').all()],
            # text = dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            line=dict(
                shape='spline',
                smoothing = 1.2
                )
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                # 'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': 'USD',
                # 'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            # margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }