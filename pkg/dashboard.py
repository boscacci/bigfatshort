import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from pkg import app
from pkg.models import *
import pdb

edu_levels = ['03','04','06','08','09']
edu_level_labels = ['No Diploma', 'HS Diploma', 'Associates', 'Bachelors', 'Masters / Dr.']

zipped_edus = list(zip(edu_level_labels, edu_levels))
edu_dict = dict(zip(edu_levels, edu_level_labels))

expense_cats = ['income', 'housing', 'foodhome','foodaway','health','alcbevg','apparel','trans','entrtain']
# expense_cats_no_gdp = ['income', 'housing', 'foodhome','foodaway','health','alcbevg','apparel','trans','entrtain']

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='expense_1',
                options=[{'label': i, 'value': i} for i in expense_cats],
                value='expense_1'
            ),
        ],style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='expense_2',
                options=[{'label': i, 'value': i} for i in expense_cats],
                value='expense_2'
            ),
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    html.Div([
        
        html.P(['Education Categories'],style={'float': 'right'}),

        html.Div([
            dcc.Graph(id='indicator-graphic')
        ],style={'width': '90%', 'float': 'left', 'display': 'inline-block'}),

        html.Div([
            dcc.Checklist(
                id = 'checkboxes',
                options=[{'label': i[0], 'value': i[1]} for i in zipped_edus],
                values=[],
        style={'width': '10%', 'float': 'right', 'display': 'inline-block'})
        ]),

        html.P(['Other Filter'],style={'float': 'right'}),

        html.Div([
            dcc.Checklist(
                id = 'gdp',
                options=[{'label': 'GDP Per Capita', 'value': 'gdp_percap'}],
                values=[],
        style={'width': '10%', 'float': 'right', 'display': 'inline-block'})
        ])
    ])
])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('checkboxes', 'values'),
     dash.dependencies.Input('gdp', 'values'),
     dash.dependencies.Input('expense_1', 'value'),
     dash.dependencies.Input('expense_2', 'value')])
    
def update_graph(checkboxes, gdp, expense_1, expense_2):
    years = list(range(2002,2013))
    traces = []
    # pdb.set_trace()
    for edu_level in checkboxes:  
        if expense_2 == 'expense_2':
            y1 = [getattr(item, expense_1) for item in By_Edu.query.filter(By_Edu.edu_level == edu_level).all()]
            trace = [go.Scatter(
                x = years,
                y = y1,
                line=dict(
                    shape='spline',
                    smoothing = 1.2
                    ),
                name = f'{edu_dict[edu_level]} {expense_1}'
            )]
            traces.extend(trace)
        elif expense_1 == 'expense_1':
            y2 = [getattr(item, expense_2) for item in By_Edu.query.filter(By_Edu.edu_level == edu_level).all()]
            trace = [go.Scatter(
                x = years,
                y = y2,
                line=dict(
                    shape='spline',
                    smoothing = 1.2
                    ),
                name = f'{edu_dict[edu_level]} {expense_2}'
            )]
            traces.extend(trace)
        else:
            y1 = [getattr(item, expense_1) for item in By_Edu.query.filter(By_Edu.edu_level == edu_level).all()]
            y2 = [getattr(item, expense_2) for item in By_Edu.query.filter(By_Edu.edu_level == edu_level).all()]
            trace = [go.Scatter(
                x = years,
                y = y1,
                line=dict(
                    shape='spline',
                    smoothing = 1.2
                    ),
                name = f'{edu_dict[edu_level]} {expense_1}'
            ),
                    go.Scatter(
                x = years,
                y = y2,
                line=dict(
                    shape='spline',
                    smoothing = 1.2
                    ),
                name = f'{edu_dict[edu_level]} {expense_2}'
            )]
            traces.extend(trace)

    if gdp:
        y1 = [item[1] for item in By_Edu.query.join(GDP_Percap, By_Edu.year == GDP_Percap.year).add_columns(GDP_Percap.gdp).filter(By_Edu.edu_level == edu_level).all()]
        name1 = "GDP_Percap"
        trace = [go.Scatter(
            x = years,
            y = y1,
            line=dict(
                shape='spline',
                smoothing = 1.2
                ),
            name = name1
        )]
        traces.extend(trace)
        

    return {
        'data': traces,

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
            hovermode='closest',
            height = 600
        )
    }