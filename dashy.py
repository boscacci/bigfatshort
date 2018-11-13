import dash
import dash_core_components as dcc
import dash_html_components as html
from sqlalchemy import *


engine = create_engine('sqlite:///blsdata.db')
conn = engine.connect()
gdp_percap = conn.execute("SELECT * FROM gdp_percap;").fetchall()
exp_by_edu3 = conn.execute("SELECT * FROM by_edu WHERE edu_level = 03;").fetchall()
exp_by_edu9 = conn.execute("SELECT * FROM by_edu WHERE edu_level = 09;").fetchall()
exp_by_housing = conn.execute("SELECT * FROM by_edu WHERE edu_level = 09;").fetchall()
years = list(range(2002, 2012))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label = 'Tab one', children=[
            dcc.Graph(
                id='example-graph1',
                figure={
                    'data': [
                        # {'x': [item[1] for item in gdp_percap], 'y': [item[2] for item in gdp_percap], 'type': 'bar', 'name': 'GDP'},
                        # {'x': [item[1] for item in exp_by_edu], 'y': [item[3] for item in exp_by_edu], 'type': 'bar', 'name': '< HS Income'},
                        # {'x': years, 'y': [item[5] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        # {'x': years, 'y': [item[7] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        {'x': years, 'y': [item[5] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        {'x': years, 'y': [item[7] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                    ],
                    'layout': {
                        'title': 'ma/phd exp'
                    }
                }
            )]),
        dcc.Tab(label = 'Tab two', children=[
            dcc.Graph(
                id='example-graph2',
                figure={
                    'data': [
                        # {'x': [item[1] for item in gdp_percap], 'y': [item[2] for item in gdp_percap], 'type': 'bar', 'name': 'GDP'},
                        # {'x': [item[1] for item in exp_by_edu], 'y': [item[3] for item in exp_by_edu], 'type': 'bar', 'name': '< HS Income'},
                        {'x': years, 'y': [item[5] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        {'x': years, 'y': [item[7] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        # {'x': years, 'y': [item[5] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        # {'x': years, 'y': [item[7] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                    ],
                    'layout': {
                        'title': '< hs exp'
                    }
                })
            ]),
        dcc.Tab(label = 'Tab three', children=[
            dcc.Graph(
                id='example-graph3',
                figure={
                    'data': [
                        # {'x': [item[1] for item in gdp_percap], 'y': [item[2] for item in gdp_percap], 'type': 'bar', 'name': 'GDP'},
                        # {'x': [item[1] for item in exp_by_edu], 'y': [item[3] for item in exp_by_edu], 'type': 'bar', 'name': '< HS Income'},
                        {'x': years, 'y': [item[5] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        {'x': years, 'y': [item[7] for item in exp_by_edu3], 'type': 'Scatter', 'name': '< HS FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        # {'x': years, 'y': [item[5] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodHome', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                        # {'x': years, 'y': [item[7] for item in exp_by_edu9], 'type': 'Scatter', 'name': 'phd FoodAway', 'line': {'shape': 'spline', 'smoothing': 1.3}},
                    ],
                    'layout': {
                        'title': '< hs exp'
                    }
                })
            ])
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)